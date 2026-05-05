"""IntelliGuard RAG Portal — Enterprise Dark Theme CSS"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

/* ═══════════════ GLOBAL DARK THEME ═══════════════ */
:root {
    --bg-root: #060a14;
    --bg-primary: #0a0f1e;
    --bg-secondary: #0d1326;
    --bg-card: #111a2e;
    --bg-card-alt: #0f1729;
    --bg-elevated: #162040;
    --bg-input: #0c1220;
    --accent-blue: #2563eb;
    --accent-cyan: #06b6d4;
    --accent-emerald: #10b981;
    --accent-red: #ef4444;
    --accent-amber: #f59e0b;
    --accent-purple: #8b5cf6;
    --glow-blue: rgba(37, 99, 235, 0.15);
    --glow-red: rgba(239, 68, 68, 0.12);
    --glow-green: rgba(16, 185, 129, 0.12);
    --text-primary: #e8edf5;
    --text-secondary: #7a8baa;
    --text-muted: #4a5878;
    --border-subtle: rgba(255,255,255,0.06);
    --border-card: rgba(255,255,255,0.08);
    --gradient-blue: linear-gradient(135deg, #2563eb, #06b6d4);
    --gradient-green: linear-gradient(135deg, #10b981, #34d399);
    --gradient-red: linear-gradient(135deg, #dc2626, #ef4444);
    --gradient-purple: linear-gradient(135deg, #7c3aed, #8b5cf6);
    --shadow-card: 0 4px 24px rgba(0,0,0,0.4);
    --shadow-glow-blue: 0 0 30px rgba(37, 99, 235, 0.15);
    --shadow-glow-red: 0 0 30px rgba(239, 68, 68, 0.15);
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: var(--bg-root) !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', -apple-system, sans-serif !important;
}

[data-testid="stAppViewContainer"] > .main {
    background: var(--bg-primary) !important;
}

[data-testid="stHeader"] {
    background: rgba(6, 10, 20, 0.85) !important;
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border-subtle);
}

/* ═══════════════ SIDEBAR ═══════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080d1c 0%, #0a1020 100%) !important;
    border-right: 1px solid var(--border-subtle) !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] span,
[data-testid="stSidebar"] .stMarkdown {
    color: var(--text-primary) !important;
}
[data-testid="stSidebar"] hr {
    border-color: var(--border-subtle) !important;
}

/* ═══════════════ LOGO AREA ═══════════════ */
.sidebar-logo {
    text-align: center;
    padding: 20px 16px 12px;
    border-bottom: 1px solid var(--border-subtle);
    margin-bottom: 16px;
}
.sidebar-logo .shield-icon {
    font-size: 2.8rem;
    display: block;
    margin-bottom: 6px;
    filter: drop-shadow(0 0 12px rgba(37, 99, 235, 0.5));
}
.sidebar-logo .brand {
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: -0.3px;
    background: var(--gradient-blue);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.sidebar-logo .sub {
    font-size: 0.68rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 2px;
}

/* Protected badge */
.protected-badge {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    margin: 12px 16px;
    padding: 8px 14px;
    border-radius: 8px;
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.25);
    font-size: 0.72rem;
    font-weight: 700;
    color: #34d399;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}
.protected-badge .dot {
    width: 7px; height: 7px;
    background: #34d399;
    border-radius: 50%;
    box-shadow: 0 0 8px #34d399;
    animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; box-shadow: 0 0 8px #34d399; }
    50% { opacity: 0.5; box-shadow: 0 0 16px #34d399; }
}

/* Sidebar section headers */
.sidebar-section {
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 16px 16px 8px;
}

/* ═══════════════ AUDIT LOG CARDS ═══════════════ */
.audit-card {
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: 10px;
    padding: 12px 14px;
    margin: 0 8px 8px;
    transition: all 0.2s ease;
}
.audit-card:hover {
    border-color: rgba(255,255,255,0.12);
    transform: translateY(-1px);
    box-shadow: var(--shadow-card);
}
.audit-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
}
.badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 10px;
    border-radius: 6px;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}
.badge-safe {
    background: rgba(16, 185, 129, 0.12);
    color: #34d399;
    border: 1px solid rgba(16, 185, 129, 0.25);
}
.badge-danger {
    background: rgba(239, 68, 68, 0.12);
    color: #f87171;
    border: 1px solid rgba(239, 68, 68, 0.25);
}
.badge-warn {
    background: rgba(245, 158, 11, 0.12);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.25);
}
.audit-time {
    font-size: 0.65rem;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
}
.audit-query-text {
    font-size: 0.78rem;
    color: var(--text-secondary);
    line-height: 1.4;
    word-break: break-word;
}
.audit-confidence {
    font-size: 0.65rem;
    color: var(--text-muted);
    margin-top: 4px;
    font-family: 'JetBrains Mono', monospace;
}

/* ═══════════════ MAIN HEADER ═══════════════ */
.main-header {
    text-align: center;
    padding: 28px 0 8px;
}
.main-header .icon-row {
    font-size: 2.2rem;
    margin-bottom: 6px;
    filter: drop-shadow(0 0 20px rgba(37, 99, 235, 0.4));
}
.main-header h1 {
    font-size: 1.9rem;
    font-weight: 900;
    color: var(--text-primary);
    letter-spacing: -0.5px;
    margin: 0;
}
.main-header .secured-by {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-top: 4px;
}
.main-header .secured-by span {
    color: var(--accent-emerald);
    font-weight: 600;
}

/* ═══════════════ METRICS BAR ═══════════════ */
.metrics-bar {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 20px 0;
}
.metric-box {
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
}
.metric-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}
.metric-box.blue::before { background: var(--gradient-blue); }
.metric-box.green::before { background: var(--gradient-green); }
.metric-box.red::before { background: var(--gradient-red); }
.metric-box.purple::before { background: var(--gradient-purple); }
.metric-box:hover {
    border-color: rgba(255,255,255,0.12);
    transform: translateY(-2px);
    box-shadow: var(--shadow-card);
}
.metric-box .number {
    font-size: 1.8rem;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    line-height: 1;
}
.metric-box.blue .number { color: #60a5fa; }
.metric-box.green .number { color: #34d399; }
.metric-box.red .number { color: #f87171; }
.metric-box.purple .number { color: #a78bfa; }
.metric-box .label {
    font-size: 0.68rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
}

/* ═══════════════ CHAT MESSAGES ═══════════════ */
.chat-container { margin: 16px 0; }

.msg-user {
    display: flex;
    justify-content: flex-end;
    margin: 12px 0;
}
.msg-user-bubble {
    background: linear-gradient(135deg, #1e3a6e, #162d5a);
    border: 1px solid rgba(37, 99, 235, 0.2);
    border-radius: 16px 16px 4px 16px;
    padding: 14px 18px;
    max-width: 75%;
    color: var(--text-primary);
    font-size: 0.9rem;
    line-height: 1.5;
    box-shadow: 0 2px 12px rgba(0,0,0,0.3);
}
.msg-user-label {
    font-size: 0.65rem;
    color: var(--text-muted);
    text-align: right;
    margin-bottom: 3px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.msg-ai {
    display: flex;
    justify-content: flex-start;
    margin: 12px 0;
}
.msg-ai-bubble {
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: 16px 16px 16px 4px;
    padding: 16px 20px;
    max-width: 82%;
    color: var(--text-primary);
    font-size: 0.9rem;
    line-height: 1.65;
    box-shadow: var(--shadow-card);
}
.msg-ai-label {
    font-size: 0.65rem;
    color: var(--accent-cyan);
    margin-bottom: 3px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.msg-sources {
    margin-top: 12px;
    padding-top: 10px;
    border-top: 1px solid var(--border-subtle);
    font-size: 0.72rem;
    color: var(--text-muted);
}
.msg-sources span {
    background: rgba(37, 99, 235, 0.1);
    border: 1px solid rgba(37, 99, 235, 0.2);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.68rem;
    color: #60a5fa;
    margin-left: 4px;
    font-family: 'JetBrains Mono', monospace;
}

/* ═══════════════ THREAT BLOCKED BANNER ═══════════════ */
.threat-banner {
    background: linear-gradient(135deg, rgba(185, 28, 28, 0.15), rgba(127, 29, 29, 0.1));
    border: 1px solid rgba(239, 68, 68, 0.3);
    border-left: 4px solid #ef4444;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 16px 0;
    box-shadow: var(--shadow-glow-red);
    animation: threat-pulse 3s ease-in-out infinite;
}
@keyframes threat-pulse {
    0%, 100% { box-shadow: 0 0 20px rgba(239,68,68,0.1); }
    50% { box-shadow: 0 0 35px rgba(239,68,68,0.2); }
}
.threat-banner .threat-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1rem;
    font-weight: 800;
    color: #f87171;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}
.threat-banner .threat-details {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 12px;
}
.threat-detail-item {
    background: rgba(0,0,0,0.25);
    border-radius: 8px;
    padding: 10px 12px;
    text-align: center;
}
.threat-detail-item .tdl {
    font-size: 0.62rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
}
.threat-detail-item .tdv {
    font-size: 0.95rem;
    font-weight: 700;
    color: #fca5a5;
    font-family: 'JetBrains Mono', monospace;
    margin-top: 2px;
}
.threat-banner .threat-msg {
    font-size: 0.82rem;
    color: #fca5a5;
    margin-top: 4px;
    line-height: 1.5;
}

/* ═══════════════ FILE UPLOAD ZONE ═══════════════ */
[data-testid="stFileUploader"] {
    background: var(--bg-card) !important;
    border: 2px dashed rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 8px !important;
    transition: border-color 0.3s;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(37, 99, 235, 0.4) !important;
}
[data-testid="stFileUploader"] label {
    color: var(--text-secondary) !important;
}

/* ═══════════════ BUTTONS ═══════════════ */
.stButton > button {
    background: var(--gradient-blue) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    padding: 8px 20px !important;
    transition: all 0.25s !important;
    box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(37, 99, 235, 0.4) !important;
}

/* ═══════════════ CHAT INPUT ═══════════════ */
[data-testid="stChatInput"] {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-card) !important;
    border-radius: 14px !important;
}
[data-testid="stChatInput"] textarea {
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

/* ═══════════════ METRICS OVERRIDE ═══════════════ */
[data-testid="stMetric"] { display: none !important; }

/* ═══════════════ SCROLLBAR ═══════════════ */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #334155; }

/* ═══════════════ MISC ═══════════════ */
[data-testid="stCaption"] { color: var(--text-muted) !important; }
.stSpinner > div { border-top-color: var(--accent-blue) !important; }
.stAlert { border-radius: 10px !important; }
</style>
"""
