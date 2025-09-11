import os
import sqlite3
import time
import uuid
from datetime import datetime

import pandas as pd
import qrcode
import streamlit as st
from PIL import Image

APP_TITLE = "Q&A"

# --- Brand farver ---
BRAND_BG = "#1f2951"     # mørkeblå baggrund
BRAND_GOLD = "#d6a550"   # detaljer/knapper
BRAND_ACCENT = "#004899" # evt. ekstra accent (ikke så meget brugt her)

# --- Robust DB-path (Cloud-safe) ---
_default_cloud_dir = "/mount/data" if os.path.isdir("/mount/data") else os.getcwd()
DB_PATH = os.environ.get("QNA_DB_PATH", os.path.join(_default_cloud_dir, "qna_streamlit.db"))

# ---------- Styling ----------
def inject_theme():
    st.markdown(
        f"""
        <style>
        :root {{
            --brand-bg: {BRAND_BG};
            --brand-gold: {BRAND_GOLD};
        }}

        /* Hele appens baggrund */
        .stApp {{
            background-color: var(--brand-bg) !important;
            color: #ffffff !important;
        }}

        /* Alle overskrifter */
        h1, h2, h3, h4, h5, h6 {{
            color: #ffffff !important;
        }}

        /* Links */
        a {{
            color: var(--brand-gold) !important;
        }}

        /* Knapper */
        .stButton>button {{
            background-color: var(--brand-gold) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.6rem 1rem !important;
            font-weight: 600 !important;
        }}
        .stButton>button:hover {{
            filter: brightness(1.1);
        }}

        /* Download-knap */
        .stDownloadButton>button {{
            background-color: var(--brand-gold) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.6rem 1rem !important;
            font-weight: 600 !important;
        }}

        /* Tekstfelter og textarea */
        textarea, .stTextInput input {{
            background-color: rgba(255,255,255,0.1) !important;
            color: #ffffff !important;
            border: 1px solid var(--brand-gold) !important;
            border-radius: 8px !important;
        }}

        /* Placeholder i tekstfelter */
        ::placeholder {{
            color: #cccccc !important;
        }}

        /* Info/alert-bokse */
        .stAlert>div {{
            background-color: rgba(255,255,255,0.1) !important;
            color: #ffffff !important;
            border-left: 6px solid var(--brand-gold) !important;
        }}

        /* Code blocks */
        code {{
            background-color: rgba(255,255,255,0.1) !important;
            color: #ffffff !important;
            padding: 2px 6px;
            border-radius: 4px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---------- Resten af app'en er uændret ----------
# ... (behold al din DB-logik, QR-kode, view_home, view_ask, view_admin og main præcis som i sidste version)
