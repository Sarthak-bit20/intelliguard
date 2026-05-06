"""
IntelliGuard RAG Portal v2 — Enterprise Dark Theme
TechCorp Employee Portal secured by 4-layer prompt injection detection.
"""

import streamlit as st
import requests, os, html
from datetime import datetime
from pathlib import Path
from io import BytesIO

import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from pypdf import PdfReader
from dotenv import load_dotenv
from styles import CUSTOM_CSS

# ── Config ──────────────────────────────────────────────────────────────
load_dotenv(Path(__file__).parent / ".env")

LLM_MODE = os.getenv("LLM_MODE", "groq")
AMD_ENDPOINT = os.getenv("AMD_ENDPOINT", "http://localhost:8000/v1")

INTELLIGUARD_URL = "http://127.0.0.1:8000/scan"
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_key_here")
GROQ_MODEL = "llama-3.3-70b-versatile"
DOCUMENTS_DIR = Path(__file__).parent / "documents"
CHROMA_DIR = Path(__file__).parent / "chroma_db"

st.set_page_config(
    page_title="TechCorp Portal · IntelliGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── Session state ───────────────────────────────────────────────────────
for key, default in [("chat_history", []), ("audit_log", [])]:
    if key not in st.session_state:
        st.session_state[key] = default


# ── Backend helpers ─────────────────────────────────────────────────────
@st.cache_resource
def init_chromadb():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    collection = client.get_or_create_collection(
        name="employee_docs", embedding_function=ef,
        metadata={"hnsw:space": "cosine"},
    )
    if collection.count() == 0:
        doc_id = 0
        for fpath in DOCUMENTS_DIR.glob("*.txt"):
            text = fpath.read_text(encoding="utf-8", errors="ignore")
            source = fpath.stem.replace("_", " ").title()
            for i, chunk in enumerate(_chunk_text(text)):
                collection.add(
                    ids=[f"doc_{doc_id}"], documents=[chunk],
                    metadatas=[{"source": source, "chunk": i, "file": fpath.name}],
                )
                doc_id += 1
    return collection


def _chunk_text(text, max_chars=1200):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, cur = [], ""
    for p in paragraphs:
        if len(cur) + len(p) + 2 > max_chars and cur:
            chunks.append(cur.strip())
            cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        chunks.append(cur.strip())
    return chunks


def add_pdf_to_collection(collection, pdf_file, filename):
    reader = PdfReader(pdf_file)
    full = "\n\n".join(page.extract_text() or "" for page in reader.pages)
    if not full.strip():
        return 0
    chunks = _chunk_text(full)
    base = collection.count()
    for i, c in enumerate(chunks):
        collection.add(
            ids=[f"pdf_{base+i}"], documents=[c],
            metadatas=[{"source": filename, "chunk": i, "file": filename}],
        )
    return len(chunks)


def scan_query(text):
    try:
        r = requests.post(INTELLIGUARD_URL, json={"text": text}, timeout=15)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        return {"verdict": "ERROR", "score": 0, "details": {"error": "API offline — start with: uvicorn main:app --port 8000"}}
    except Exception as e:
        return {"verdict": "ERROR", "score": 0, "details": {"error": str(e)}}


def ask_llm(query, context_chunks):
    context = "\n\n---\n\n".join(context_chunks)
    system_prompt = (
        "You are TechCorp's AI assistant. Answer using ONLY the provided context. "
        "If the answer isn't in context, say so. Be concise and professional. Use bullet points."
    )
    messages = [
        {"role": "user", "content": f"Context:\n{context}\n\n---\nQuestion: {query}"}
    ]
    try:
        if LLM_MODE == "amd":
            from openai import OpenAI
            client = OpenAI(base_url=AMD_ENDPOINT, api_key="not-required")
            r = client.chat.completions.create(
                model="Qwen/Qwen2.5-7B-Instruct",
                messages=[{"role": "system", "content": system_prompt}] + messages,
                temperature=0.3,
                max_tokens=1024,
            )
        else:
            client = Groq(api_key=GROQ_API_KEY)
            r = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[{"role": "system", "content": system_prompt}] + messages,
                temperature=0.3,
                max_tokens=1024,
            )
        return r.choices[0].message.content
    except Exception as e:
        return f"⚠️ LLM Error: {e}"


def log_audit(query, verdict, score, source="chat"):
    st.session_state.audit_log.insert(0, {
        "ts": datetime.now().strftime("%H:%M:%S"),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "query": query[:100], "verdict": verdict,
        "score": round(score, 4), "source": source,
    })


# ═══════════════════════════════════════════════════════════════════
#  SIDEBAR
# ═══════════════════════════════════════════════════════════════════
with st.sidebar:
    # Logo
    st.markdown("""
    <div class="sidebar-logo">
        <span class="shield-icon">🛡️</span>
        <div class="brand">INTELLIGUARD</div>
        <div class="sub">Security Platform</div>
    </div>
    """, unsafe_allow_html=True)

    # Protected badge
    st.markdown("""
    <div class="protected-badge">
        <span class="dot"></span> IntelliGuard Protected
    </div>
    """, unsafe_allow_html=True)

    # Audit Log section
    st.markdown('<div class="sidebar-section">📋 Audit Log</div>', unsafe_allow_html=True)

    if st.session_state.audit_log:
        for entry in st.session_state.audit_log[:30]:
            v = entry["verdict"]
            badge_cls = "badge-safe" if v == "SAFE" else "badge-danger" if v == "INJECTION" else "badge-warn"
            icon = "✓" if v == "SAFE" else "✕" if v == "INJECTION" else "!"
            q = html.escape(entry["query"])
            st.markdown(f"""
            <div class="audit-card">
                <div class="audit-card-header">
                    <span class="badge {badge_cls}">{icon} {v}</span>
                    <span class="audit-time">{entry['ts']}</span>
                </div>
                <div class="audit-query-text">{q}</div>
                <div class="audit-confidence">confidence: {entry['score']:.2%} · {entry['source']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.caption("No activity recorded yet.")

    st.markdown("---")

    # Upload section
    st.markdown('<div class="sidebar-section">📄 Document Upload</div>', unsafe_allow_html=True)
    uploaded = st.file_uploader("Drop a PDF to add to knowledge base", type=["pdf"], key="pdf_up")
    if uploaded and st.button("🔍 Scan & Ingest", use_container_width=True):
        reader = PdfReader(uploaded)
        sample = " ".join((p.extract_text() or "")[:500] for p in reader.pages[:3])
        with st.spinner("Scanning with IntelliGuard..."):
            res = scan_query(sample)
        v, s = res.get("verdict", "ERROR"), res.get("score", 0)
        log_audit(f"[PDF] {uploaded.name}", v, s, "upload")
        if v == "INJECTION":
            st.error(f"🚨 Blocked — malicious content in `{uploaded.name}` ({s:.0%})")
        elif v == "ERROR":
            st.warning(f"⚠️ {res['details'].get('error','Unknown')}")
        else:
            with st.spinner("Indexing..."):
                n = add_pdf_to_collection(init_chromadb(), uploaded, uploaded.name)
            st.success(f"✅ {uploaded.name} — {n} chunks added")


# ═══════════════════════════════════════════════════════════════════
#  MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════

# Header
st.markdown("""
<div class="main-header">
    <div class="icon-row">🛡️</div>
    <h1>TechCorp Employee Portal</h1>
    <div class="secured-by">Secured by <span>IntelliGuard</span> · 4-Layer Prompt Injection Detection</div>
</div>
""", unsafe_allow_html=True)

# Metrics bar
collection = init_chromadb()
total_q = len(st.session_state.audit_log)
safe_q = sum(1 for a in st.session_state.audit_log if a["verdict"] == "SAFE")
blocked_q = sum(1 for a in st.session_state.audit_log if a["verdict"] == "INJECTION")
accuracy = (safe_q / total_q * 100) if total_q > 0 else 100.0

st.markdown(f"""
<div class="metrics-bar">
    <div class="metric-box blue">
        <div class="number">{total_q}</div>
        <div class="label">Total Queries</div>
    </div>
    <div class="metric-box red">
        <div class="number">{blocked_q}</div>
        <div class="label">Threats Blocked</div>
    </div>
    <div class="metric-box green">
        <div class="number">{safe_q}</div>
        <div class="label">Safe Queries</div>
    </div>
    <div class="metric-box purple">
        <div class="number">{accuracy:.0f}%</div>
        <div class="label">Safe Rate</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="msg-user">
            <div>
                <div class="msg-user-label">You</div>
                <div class="msg-user-bubble">{html.escape(msg['content'])}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    elif msg["role"] == "blocked":
        score = msg.get("score", 0)
        spine = msg.get("spine", 0)
        brain = msg.get("brain", 0)
        st.markdown(f"""
        <div class="threat-banner">
            <div class="threat-title">🚨 THREAT BLOCKED</div>
            <div class="threat-msg">Prompt injection attempt detected and neutralized. This query has been logged for security review.</div>
            <div class="threat-details">
                <div class="threat-detail-item">
                    <div class="tdl">Confidence</div>
                    <div class="tdv">{score:.1%}</div>
                </div>
                <div class="threat-detail-item">
                    <div class="tdl">SPINE Score</div>
                    <div class="tdv">{spine:.1%}</div>
                </div>
                <div class="threat-detail-item">
                    <div class="tdl">BRAIN Score</div>
                    <div class="tdv">{brain:.1%}</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

    elif msg["role"] == "assistant":
        content = msg["content"]
        sources_html = ""
        if msg.get("sources"):
            tags = "".join(f'<span>{html.escape(s)}</span>' for s in msg["sources"])
            sources_html = f'<div class="msg-sources">📎 Sources: {tags}</div>'
        st.markdown(f"""
        <div class="msg-ai">
            <div>
                <div class="msg-ai-label">🤖 IntelliGuard AI</div>
                <div class="msg-ai-bubble">{html.escape(content)}{sources_html}</div>
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Chat input
query = st.chat_input("Ask about company policies, benefits, security guidelines...")

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})

    with st.spinner("🔍 IntelliGuard scanning..."):
        scan = scan_query(query)

    verdict = scan.get("verdict", "ERROR")
    score = scan.get("score", 0)
    details = scan.get("details", {})
    spine = details.get("spine_score", 0) or 0
    brain = details.get("brain_score", 0) or 0
    log_audit(query, verdict, score, "chat")

    if verdict == "INJECTION":
        st.session_state.chat_history.append({
            "role": "blocked", "content": query,
            "score": score, "spine": spine, "brain": brain,
        })
    elif verdict == "ERROR":
        err = details.get("error", "Unknown")
        st.session_state.chat_history.append({
            "role": "assistant", "content": f"⚠️ Security scan unavailable: {err}",
            "sources": [],
        })
    else:
        with st.spinner("📚 Retrieving knowledge..."):
            results = collection.query(query_texts=[query], n_results=5)
            chunks = results["documents"][0] if results["documents"] else []
            metas = results["metadatas"][0] if results["metadatas"] else []

        with st.spinner("🧠 Generating response..."):
            answer = ask_llm(query, chunks)

        sources = list({m.get("source", "Unknown") for m in metas})
        st.session_state.chat_history.append({
            "role": "assistant", "content": answer, "sources": sources,
        })

    st.rerun()
