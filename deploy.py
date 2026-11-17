import streamlit as st
import os
from pathlib import Path

# ======================================================================
#  STREAMLIT SEITEN-KONFIGURATION & CSS DESIGN
# ======================================================================
st.set_page_config(
    page_title="Lokal & Verschlüsselt",
    page_icon="🔒",
    layout="centered"
)

# Design anpassen: Schwarzer Hintergrund, Times New Roman, weiße Schrift
st.markdown("""
    <style>
    /* Globaler Hintergrund & Schriftart */
    .stApp {
        background-color: #0B0F14;
        color: #FFFFFF;
        font-family: "Times New Roman", Times, serif, sans-serif;
    }

    /* Alle Überschriften & Texte auf Times New Roman und Weiß zwingen */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        font-family: "Times New Roman", Times, serif !important;
        color: #FFFFFF !important;
    }

    /* Slogan zentrieren und stylen */
    .slogan {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 30px;
        letter-spacing: 0.5px;
    }

    /* Container für zentrierte Elemente */
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# ======================================================================
#  BENutzerdefinierter Slogan
# ======================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="slogan">Deine Sicherheit, Dein Gerät - lokal und verschlüsselt.</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ======================================================================
#  APP-ICON (PNG) ANZEIGEN
# ======================================================================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    icon_path = Path("icon.png")
    if icon_path.exists():
        # Bild wird zentriert und in passender Größe angezeigt
        st.image(str(icon_path), use_column_width=True)
    else:
        st.warning("⚠️ Die Datei 'icon.png' wurde im Verzeichnis nicht gefunden.")

st.markdown("<br>", unsafe_allow_html=True)

# ======================================================================
#  DATEI-DOWNLOAD BEREICH
# ======================================================================
# ======================================================================
#  HIER DATEIPFAD EINFÜGEN (LÜCKE FÜR DEINE DATEI)
# ======================================================================
# Trage hier den relativen oder absoluten Pfad zu der Datei ein,
# die heruntergeladen werden soll (z.B. eine .zip, .exe oder .dmg Datei).
FILE_TO_DOWNLOAD = "PasswortManager_Installer.zip"  # <-- HIER PFAD ANPASSEN
# ======================================================================

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    file_path = Path(FILE_TO_DOWNLOAD)

    if file_path.exists():
        with open(file_path, "rb") as file:
            file_bytes = file.read()

        st.download_button(
            label="📥 Datei herunterladen",
            data=file_bytes,
            file_name=file_path.name,
            mime="application/octet-stream",
            use_container_width=True
        )
    else:
        # Falls die Zieldatei (noch) nicht existiert, wird ein Info-Hinweis angezeigt
        st.error(f"❌ Datei nicht gefunden: `{FILE_TO_DOWNLOAD}`")
        st.info("Bitte passe den `FILE_TO_DOWNLOAD`-Pfad im Code an und lege die Datei bereit.")
