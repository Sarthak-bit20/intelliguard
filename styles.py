CUSTOM_CSS = """<style>
/* ══════════════════════════════════════════════════════════════════
   IntelliGuard — Enterprise Dark Theme
   Pure CSS, injected via st.markdown with <style> tags
   ══════════════════════════════════════════════════════════════════ */

/* ── Import Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ── Base Reset ── */
*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background-color: #06090f !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* Main content area */
.block-container {
    padding: 1rem 2rem 2rem 2rem !important;
    max-width: 1200px !important;
}

/* ── Hide Streamlit branding ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] {
    background: rgba(6, 9, 15, 0.9) !important;
    backdrop-filter: blur(10px);
}

/* ══════════════════════════════════════
   SIDEBAR
   ══════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b0f1a 0%, #0d1220 100%) !important;
    border-right: 1px solid #1a2235 !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding: 1.5rem 1rem !important;
}

/* Sidebar text defaults */
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown span {
    color: #94a3b8 !important;
}
[data-testid="stSidebar"] .stCaption p {
    color: #4b5563 !important;
}

/* ── Sidebar Logo ── */
.sidebar-logo {
    text-align: center;
    padding: 1.2rem 0 1.8rem 0;
    border-bottom: 1px solid #1a2235;
    margin-bottom: 1.5rem;
}
.shield-icon {
    font-size: 2.8rem;
    display: block;
    margin-bottom: 0.5rem;
    filter: drop-shadow(0 0 12px rgba(96, 165, 250, 0.3));
}
.brand {
    font-size: 1.05rem;
    font-weight: 800;
    letter-spacing: 0.18em;
    color: #60a5fa;
    font-family: 'Inter', sans-serif;
}
.sub {
    font-size: 0.6rem;
    color: #475569;
    letter-spacing: 0.22em;
    margin-top: 3px;
    text-transform: uppercase;
}

/* ── Protected Badge ── */
.protected-badge {
    background: rgba(16, 185, 129, 0.06);
    border: 1px solid rgba(16, 185, 129, 0.25);
    color: #10b981;
    padding: 0.45rem 1rem;
    border-radius: 20px;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-align: center;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}
.dot {
    width: 7px;
    height: 7px;
    background: #10b981;
    border-radius: 50%;
    display: inline-block;
    animation: pulse 2s ease-in-out infinite;
    box-shadow: 0 0 6px rgba(16, 185, 129, 0.4);
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.35; transform: scale(0.85); }
}

/* ── Sidebar Section Headers ── */
.sidebar-section {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    color: #475569;
    margin: 1.4rem 0 0.7rem 0;
    text-transform: uppercase;
    font-family: 'Inter', sans-serif;
}

/* ── Audit Cards ── */
.audit-card {
    background: #111827;
    border: 1px solid #1a2235;
    border-radius: 8px;
    padding: 0.65rem 0.85rem;
    margin-bottom: 0.45rem;
    transition: all 0.2s ease;
}
.audit-card:hover {
    border-color: #2d3a50;
    background: #131c2e;
}
.audit-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
}
.audit-time {
    font-size: 0.6rem;
    color: #475569;
    font-family: 'Inter', monospace;
}
.audit-query-text {
    font-size: 0.7rem;
    color: #94a3b8;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 220px;
}
.audit-confidence {
    font-size: 0.6rem;
    color: #475569;
    margin-top: 3px;
}
.audit-category {
    font-size: 0.6rem;
    color: #a78bfa;
    margin-top: 3px;
    font-weight: 500;
}

/* ── Verdict Badges ── */
.badge {
    font-size: 0.55rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 99px;
    letter-spacing: 0.05em;
    display: inline-block;
    text-transform: uppercase;
}
.badge-safe {
    background: rgba(16,185,129,0.1);
    color: #10b981;
    border: 1px solid rgba(16,185,129,0.2);
}
.badge-danger {
    background: rgba(239,68,68,0.1);
    color: #ef4444;
    border: 1px solid rgba(239,68,68,0.2);
}
.badge-warn {
    background: rgba(234,179,8,0.1);
    color: #eab308;
    border: 1px solid rgba(234,179,8,0.2);
}

/* ══════════════════════════════════════
   MAIN CONTENT AREA
   ══════════════════════════════════════ */

/* ── Main Header ── */
.main-header {
    text-align: center;
    padding: 2.5rem 1rem 2rem 1rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid #1a2235;
}
.icon-row {
    font-size: 2.8rem;
    margin-bottom: 0.6rem;
    filter: drop-shadow(0 0 16px rgba(96, 165, 250, 0.2));
}
.main-header h1 {
    font-size: 1.7rem;
    font-weight: 800;
    color: #f1f5f9;
    margin: 0 0 0.4rem 0;
    font-family: 'Inter', sans-serif;
    letter-spacing: -0.01em;
}
.secured-by {
    font-size: 0.78rem;
    color: #4b5563;
    font-weight: 400;
}
.secured-by span {
    color: #10b981;
    font-weight: 600;
}

/* ── Metrics Bar ── */
.metrics-bar {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.8rem;
    margin-bottom: 2rem;
}
.metric-box {
    background: #0f172a;
    border-radius: 10px;
    padding: 1.1rem 0.8rem;
    text-align: center;
    border: 1px solid #1a2235;
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
}
.metric-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
}
.metric-box:hover {
    transform: translateY(-3px);
    border-color: #2d3a50;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.metric-box.blue::before { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
.metric-box.red::before { background: linear-gradient(90deg, #ef4444, #f87171); }
.metric-box.green::before { background: linear-gradient(90deg, #10b981, #34d399); }
.metric-box.purple::before { background: linear-gradient(90deg, #8b5cf6, #a78bfa); }
.metric-box .number {
    font-size: 1.8rem;
    font-weight: 800;
    color: #f1f5f9;
    font-family: 'Inter', sans-serif;
    line-height: 1;
    margin-bottom: 4px;
}
.metric-box .label {
    font-size: 0.6rem;
    color: #4b5563;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 600;
}

/* ── Chat Container ── */
.chat-container {
    min-height: 200px;
    max-height: 450px;
    overflow-y: auto;
    margin-bottom: 0.5rem;
    padding: 0.5rem 0;
}

/* ── Chat Bubbles ── */
.msg-user {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;
}
.msg-user-bubble {
    background: linear-gradient(135deg, #1e3a5f, #1a3355);
    border: 1px solid #2d4f7c;
    color: #e2e8f0;
    padding: 0.75rem 1rem;
    border-radius: 14px 14px 3px 14px;
    max-width: 70%;
    font-size: 0.84rem;
    line-height: 1.55;
}
.msg-user-label {
    font-size: 0.62rem;
    color: #4b5563;
    text-align: right;
    margin-bottom: 4px;
    font-weight: 500;
}

.msg-ai {
    display: flex;
    margin-bottom: 1rem;
}
.msg-ai-bubble {
    background: #111827;
    border: 1px solid #1a2235;
    color: #d1d5db;
    padding: 0.75rem 1rem;
    border-radius: 14px 14px 14px 3px;
    max-width: 80%;
    font-size: 0.84rem;
    line-height: 1.6;
}
.msg-ai-label {
    font-size: 0.62rem;
    color: #4b5563;
    margin-bottom: 4px;
    font-weight: 500;
}
.msg-sources {
    font-size: 0.68rem;
    color: #4b5563;
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px solid #1a2235;
}
.msg-sources span {
    background: #1a2235;
    padding: 2px 7px;
    border-radius: 4px;
    margin-right: 4px;
    font-size: 0.62rem;
    color: #94a3b8;
}

/* ── Threat Banner ── */
.threat-banner {
    background: linear-gradient(135deg, rgba(239,68,68,0.07), rgba(239,68,68,0.02));
    border: 1px solid rgba(239,68,68,0.25);
    border-left: 3px solid #ef4444;
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 1rem;
    animation: threatSlideIn 0.35s ease-out;
}
@keyframes threatSlideIn {
    from { opacity: 0; transform: translateY(-6px); }
    to { opacity: 1; transform: translateY(0); }
}
.threat-title {
    color: #ef4444;
    font-weight: 700;
    font-size: 0.88rem;
    margin-bottom: 4px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.threat-category {
    color: #a78bfa;
    font-size: 0.76rem;
    margin: 4px 0;
    font-weight: 500;
}
.threat-msg {
    font-size: 0.76rem;
    color: #94a3b8;
    margin-bottom: 0.9rem;
    line-height: 1.4;
}
.threat-details {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.6rem;
}
.threat-detail-item {
    text-align: center;
    background: rgba(239,68,68,0.04);
    border-radius: 6px;
    padding: 0.5rem 0.3rem;
}
.tdl {
    font-size: 0.55rem;
    color: #4b5563;
    letter-spacing: 0.1em;
    margin-bottom: 3px;
    text-transform: uppercase;
    font-weight: 600;
}
.tdv {
    font-size: 1rem;
    font-weight: 700;
    color: #ef4444;
    font-family: 'Inter', sans-serif;
}
.threat-intent {
    background: rgba(167, 139, 250, 0.08);
    border: 1px solid rgba(167, 139, 250, 0.2);
    border-radius: 6px;
    padding: 0.6rem;
    margin: 0.8rem 0;
    font-size: 0.74rem;
    color: #a78bfa;
    line-height: 1.4;
}
.obfuscation-tag {
    background: rgba(245, 158, 11, 0.1);
    color: #f59e0b;
    border: 1px solid rgba(245, 158, 11, 0.25);
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 0.62rem;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 8px;
    text-transform: uppercase;
}
.metric-box.orange::before { background: linear-gradient(90deg, #f59e0b, #fbbf24); }

/* ══════════════════════════════════════
   STREAMLIT COMPONENT OVERRIDES
   ══════════════════════════════════════ */

/* ── Bottom container (chat input dock) — aggressive overrides ── */
[data-testid="stBottom"],
[data-testid="stBottom"] *,
[data-testid="stBottomBlockContainer"],
[data-testid="stBottomBlockContainer"] > div,
[data-testid="stBottomBlockContainer"] > div > div,
.stChatInput,
.stBottom,
div[data-testid="stBottom"] > div {
    background-color: #06090f !important;
    background: #06090f !important;
}

/* ── Chat Input ── */
[data-testid="stChatInput"] {
    padding: 0 !important;
    background: #06090f !important;
}
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] > div > div {
    background-color: #0f172a !important;
    border: 1.5px solid #2d3a50 !important;
    border-radius: 12px !important;
    transition: border-color 0.2s ease;
}
[data-testid="stChatInput"] > div:focus-within,
[data-testid="stChatInput"] > div > div:focus-within {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.15) !important;
}
[data-testid="stChatInputTextArea"],
[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] input {
    color: #f1f5f9 !important;
    background-color: #0f172a !important;
    caret-color: #60a5fa !important;
    -webkit-text-fill-color: #f1f5f9 !important;
    font-size: 0.88rem !important;
    font-family: 'Inter', sans-serif !important;
    border: none !important;
}
[data-testid="stChatInput"] textarea::placeholder,
[data-testid="stChatInput"] input::placeholder {
    color: #4b5563 !important;
    -webkit-text-fill-color: #4b5563 !important;
}
[data-testid="stChatInput"] button {
    background: #4f46e5 !important;
    border-radius: 8px !important;
    color: white !important;
    border: none !important;
    transition: background 0.2s ease;
}
[data-testid="stChatInput"] button:hover {
    background: #4338ca !important;
}
[data-testid="stChatInput"] button svg {
    fill: white !important;
}

/* Force dark on any iframe-like Streamlit containers */
.stApp > div,
.stApp > div > div,
section[data-testid="stMain"],
section[data-testid="stMain"] > div {
    background-color: #06090f !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #4f46e5, #4338ca) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    padding: 0.55rem 1.2rem !important;
    transition: all 0.2s ease !important;
    font-family: 'Inter', sans-serif !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #4338ca, #3730a3) !important;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3) !important;
    transform: translateY(-1px) !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    background: #0f172a !important;
    border: 1px solid #1a2235 !important;
    border-radius: 10px !important;
    overflow: hidden;
}
[data-testid="stExpander"] summary {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
}
[data-testid="stExpander"] summary:hover {
    color: #f1f5f9 !important;
}

/* ── File Uploader ── */
[data-testid="stFileUploader"],
[data-testid="stFileUploader"] > div,
[data-testid="stFileUploader"] section,
[data-testid="stFileUploadDropzone"] {
    background: #0f172a !important;
    background-color: #0f172a !important;
    border: 1px dashed #2d3a50 !important;
    border-radius: 10px !important;
    color: #94a3b8 !important;
}
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] span {
    color: #4b5563 !important;
    font-size: 0.72rem !important;
}
[data-testid="stFileUploader"] small {
    color: #374151 !important;
}
[data-testid="stFileUploader"] button,
[data-testid="stFileUploadDropzone"] button {
    background: #1a2235 !important;
    color: #94a3b8 !important;
    border: 1px solid #2d3a50 !important;
    border-radius: 6px !important;
}
[data-testid="stFileUploader"] button:hover {
    background: #2d3a50 !important;
    color: #e2e8f0 !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #4f46e5 !important;
}

/* ── Divider ── */
hr {
    border-color: #1a2235 !important;
    opacity: 0.5;
}

/* ── Progress bar ── */
[data-testid="stProgress"] > div > div {
    background-color: #1a2235 !important;
}
[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #4f46e5, #6366f1) !important;
}

/* ── Toast / Alerts ── */
[data-testid="stAlert"] {
    border-radius: 8px !important;
}

/* ── Markdown text ── */
.stMarkdown p, .stMarkdown li {
    color: #cbd5e1;
}
.stMarkdown strong {
    color: #f1f5f9;
}

/* ── Batch Scanner Result Card ── */
.batch-result-card {
    background: #0f172a;
    border: 1px solid #1a2235;
    border-radius: 10px;
    padding: 1.2rem;
    margin-top: 0.8rem;
}
.batch-result-title {
    color: #10b981;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 1rem;
    letter-spacing: 0.03em;
}
.batch-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.8rem;
    margin-bottom: 1rem;
}
.batch-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.8rem;
}
.batch-stat {
    text-align: center;
    background: #111827;
    border-radius: 8px;
    padding: 0.8rem 0.5rem;
    border: 1px solid #1a2235;
}
.batch-stat-label {
    font-size: 0.55rem;
    color: #4b5563;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 3px;
}
.batch-stat-value {
    font-size: 1.4rem;
    font-weight: 700;
    font-family: 'Inter', sans-serif;
}
.batch-stat-value.white { color: #f1f5f9; }
.batch-stat-value.red { color: #ef4444; }
.batch-stat-value.green { color: #10b981; }
.batch-stat-value.purple { color: #a78bfa; }

/* ── Category Row ── */
.cat-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.45rem 0.75rem;
    background: #111827;
    border-radius: 6px;
    margin: 0.25rem 0;
    border: 1px solid #1a2235;
    transition: background 0.15s ease;
}
.cat-row:hover {
    background: #131c2e;
}
.cat-name {
    color: #a78bfa;
    font-size: 0.72rem;
    font-weight: 500;
}
.cat-count {
    color: #e2e8f0;
    font-size: 0.72rem;
    font-weight: 600;
}

/* ══════════════════════════════════════
   SCROLLBAR
   ══════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: #1a2235;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: #2d3a50; }

/* ── Selection Color ── */
::selection {
    background: rgba(79, 70, 229, 0.3);
    color: #f1f5f9;
}
</style>"""
