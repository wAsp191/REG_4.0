# =========================================================
# SEZIONE IMPORT
# =========================================================
import streamlit as st
import pandas as pd
import datetime
import time
from zoneinfo import ZoneInfo
from database import *

# =========================================================
# 0. CONFIGURAZIONE PAGINA (Deve essere la prima istruzione Streamlit)
# =========================================================
st.set_page_config(page_title="Technical Generator v2.0", layout="wide")


# =========================================================
# 1. FUNZIONI DI SUPPORTO (CSS, AUTH & RESET)
# =========================================================

def inject_custom_css():
    """Inietta lo stile CSS personalizzato."""
    st.markdown("""
        <style>
            .block-container {
                padding-top: 2.5rem !important;
                padding-bottom: 0rem !important;
            }
            [data-testid="stVerticalBlock"] > div {
                flex-direction: column;
                gap: 0.12rem !important;
            }
            h1 { margin-bottom: -1rem !important; font-size: 1.6rem !important; }
            h2 { margin-bottom: -0.8rem !important; font-size: 1.2rem !important; }
            h3 { margin-bottom: -0.5rem !important; font-size: 1.0rem !important; }
            hr {
                margin-top: 0.35rem !important;
                margin-bottom: 0.35rem !important;
            }
            div[data-baseweb="select"] > div, 
            div[data-testid="stTextInput"] > div > div > input {
                padding-top: 0px !important;
                padding-bottom: 0px !important;
                min-height: 1.6rem !important;
            }
            [data-testid="stWidgetLabel"] p {
                font-size: 1.4rem !important;
                font-weight: 700 !important;
            }
            [data-testid="stMarkdownContainer"] p {
                font-size: 1.1rem !important;
            }
        </style>
    """, unsafe_allow_html=True)


UTENTI_AUTORIZZATI = {
    "admin": {"password": "reg2026", "nome": "Amministratore di Sistema"},
    "pierluigi.giorgi": {"password": "pierluigigiorgi", "nome": "Pierluigi Giorgi (Ufficio Tecnico)"},
    "gaia.gualtieri": {"password": "gaiagualtieri", "nome": "Gaia Gualtieri (Ufficio Tecnico)"},
    "emanuela.bois": {"password": "emanuelabois", "nome": "Emanuela Bois (Ufficio Tecnico)"},
    "andrea.parrini": {"password": "andreaparrini", "nome": "Andrea Parrini (Ufficio Tecnico)"},
    "gianfranco.palmisano": {"password": "gianfrancopalmisano", "nome": "Gianfranco Palmisano (Ufficio Tecnico)"},
    "giuseppe.pieri": {"password": "giuseppepieri", "nome": "Giuseppe Pieri (Ufficio Tecnico)"},
    "carlo.castellani": {"password": "carlocastellani", "nome": "Carlo Castellani (Ufficio Tecnico)"},
    "enrico.sarti": {"password": "enricosarti", "nome": "Enrico Sarti (Ufficio Tecnico)"},
    "alberto.morana": {"password": "albertomorana", "nome": "Alberto Morana (Ufficio Tecnico)"}
}

def check_authentication():
    """Gestisce lo stato di login e mostra la schermata di accesso se non autenticato."""
    if "autenticato" not in st.session_state:
        st.session_state.autenticato = False
    if "utente_corrente" not in st.session_state:
        st.session_state.utente_corrente = ""

    if not st.session_state.autenticato:
        col_spazio_sx, col_login_centro, col_spazio_dx = st.columns([1, 1.5, 1])
        with col_login_centro:
            with st.container(border=True):
                st.markdown("<h2 style='text-align: center;'>🔐 Accesso - REG 2.0</h2>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center; color: gray; font-size: 0.9rem;'>Inserisci le tue credenziali</p>", unsafe_allow_html=True)
                
                with st.form("form_login"):
                    username_input = st.text_input("Username").strip().lower()
                    password_input = st.text_input("Password", type="password")
                    btn_login = st.form_submit_button("🔑 Accedi", use_container_width=True)
                    
                    if btn_login:
                        if username_input in UTENTI_AUTORIZZATI and UTENTI_AUTORIZZATI[username_input]["password"] == password_input:
                            st.session_state.autenticato = True
                            st.session_state.utente_corrente = UTENTI_AUTORIZZATI[username_input]["nome"]
                            st.rerun()
                        else:
                            st.error("❌ Credenziali non valide. Riprova.")
        st.stop()


def activate_reset():
    """Pulisce la sessione per resettare la maschera."""
    defaults = {
        'comp_tags': None,
        'selectbox_part': None,
        'extra_tags': [],
        'check_1090': False,
        'stringa_tecnica': "",
        'stringa_commerciale': "",
        'generazione_effettuata': False
    }
    text_keys = ['dim_l', 'dim_p', 'dim_h', 'dim_dia', 'dim_s', 'extra_text', 'select_finitura']
    for key, val in defaults.items():
        st.session_state[key] = val
    for key in text_keys:
        if key in st.session_state:
            st.session_state[key] = ""
    for key in list(st.session_state.keys()):
        if key.startswith("dyn_") or key.startswith("text_"):
            del st.session_state[key]
    st.session_state['reset_eseguito'] = True


# =========================================================
# ESECUZIONE INIZIALE (Iniezione CSS e Login)
# =========================================================
inject_custom_css()
check_authentication()

if st.session_state.get('reset_eseguito'):
    st.toast("Interfaccia pulita!", icon="✨")
    st.session_state['reset_eseguito'] = False


# =========================================================
# 2. INTERFACCIA UTENTE (Layout & Logica)
# =========================================================
col_t, col_r = st.columns([3.5, 1], vertical_alignment="bottom")

with col_t: 
    st.markdown("""
        <div>
            <h1 style="margin: 0; font-size: 1.8rem;">⚙️ REG - Title Generator</h1>
        </div>
    """, unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 0.85rem; color: gray; margin-top: 4px;'>Utente attivo: <b>{st.session_state.utente_corrente}</b></p>", unsafe_allow_html=True)

with col_r: 
    st.button("🔄 AZZERA", on_click=activate_reset, use_container_width=True)

st.markdown("---")

col_left, col_workarea = st.columns([1, 3.5], gap="large")

# Colonna Sinistra: Scelta Macro Categoria
with col_left:
    st.subheader("📂 1. Categoria")
    mappa_estetica = {
        "SALES PART": "⚙️ SALES PART",
        "PACKAGE PART": "📦 PACKAGE PART", 
        "LEGNO": "🪵 LEGNO"
    }
    macro_selezionata = st.radio(
        "Seleziona categoria:", 
        options=list(DATABASE.keys()), 
        format_func=lambda x: mappa_estetica.get(x, x), 
        key="radio_macro", 
        label_visibility="collapsed"
    )

# Colonna Destra: Workarea Configurazione
with col_workarea:
    st.subheader("🛠️ 2. Selezione Articolo & Finitura")
    c_art, c_fin = st.columns([1.5, 1])
    
    articoli_categoria = DATABASE.get(macro_selezionata, {}).get("Articoli", {})
    
    with c_art:
        articolo_scelto = st.selectbox(
            "Cerca Articolo:", 
            options=sorted(list(articoli_categoria.keys())), 
            index=None, 
            placeholder="Seleziona un articolo...", 
            format_func=lambda x: f"🔧 {x}" if x else "Seleziona...", 
            key="selectbox_part"
        )

    finitura_scelta = None
    if articolo_scelto:
        dati_articolo = articoli_categoria.get(articolo_scelto, {})
        ha_finitura = dati_articolo.get("ha_finitura", False)
        
        with c_fin:
            if ha_finitura:
                finitura_scelta = st.selectbox(
                    "Finitura / Materiale:",
                    options=list(FINITURE_CONFIG.keys()),
                    index=0,
                    key="select_finitura"
                )

    st.markdown("---")
    
    # Sezione 3: Caratteristiche & Pills ordinati
    st.subheader("✨ 3. Caratteristiche & Pills")
    
    if articolo_scelto:
        pills_config_articolo = dati_articolo.get("pills_config", {})
        
        if pills_config_articolo:
            pills_ordinati = sorted(
                pills_config_articolo.keys(),
                key=lambda x: pills_config_articolo[x].get("ordine", 99)
            )
            
            col_pills_sel, col_pills_dyn = st.columns([1.7, 1.3], gap="medium")
            
            with col_pills_sel:
                tag_selezionati = st.multiselect(
                    "Seleziona Caratteristiche:",
                    options=pills_ordinati,
                    key="extra_tags",
                    placeholder="Scegli le caratteristiche..."
                )
            
            with col_pills_dyn:
                tags_correnti = st.session_state.get('extra_tags', [])
                if tags_correnti:
                    st.markdown("<p style='font-size: 0.9rem; font-weight: 600; color: #ff4b4b; margin-bottom: 5px;'>⚙️ Opzioni Caratteristiche:</p>", unsafe_allow_html=True)
                    
                    for tag in tags_correnti:
                        if tag in SUB_OPTIONS_CONFIG or f"{tag} (+)" in SUB_OPTIONS_CONFIG:
                            key_sub = tag if tag in SUB_OPTIONS_CONFIG else f"{tag} (+)"
                            config_sub = SUB_OPTIONS_CONFIG[key_sub]
                            
                            if "Compatibilità piede de base" in tag or "Compatibilità piede di base" in tag:
                                col_alt, col_lung = st.columns(2)
                                with col_alt:
                                    st.selectbox("Altezza:", options=list(config_sub.get("altezze", {}).keys()), key=f"dyn_alt_{tag}")
                                with col_lung:
                                    st.selectbox("Lunghezza:", options=list(config_sub.get("lunghezze", {}).keys()), key=f"dyn_lung_{tag}")
                            else:
                                st.selectbox(
                                    f"Scelta per **{tag}**:",
                                    options=list(config_sub.keys()),
                                    key=f"dyn_val_{tag}"
                                )
        else:
            st.info("ℹ️ Nessuna caratteristica speciale configurata per questo articolo.")
    else:
        st.info("👈 Seleziona un articolo in alto per configurarne le caratteristiche.")

    st.markdown("---")
    
    # Sezione 4: Dimensioni e Note
    st.subheader("📏 4. Dimensioni e Note")
    c_dim1, c_dim2, c_dim3, c_dim4, c_dim5 = st.columns(5)
    with c_dim1: st.text_input("Lunghezza (L):", key="dim_l")
    with c_dim2: st.text_input("Profondità (P):", key="dim_p")
    with c_dim3: st.text_input("Altezza (H):", key="dim_h")
    with c_dim4: st.text_input("Diametro (Ø):", key="dim_dia")
    with c_dim5: st.text_input("Spessore (SP):", key="dim_s")

    st.text_input("Note libere / Specifiche extra:", key="extra_text")
    st.checkbox("Aggiungi marcatura (UNI EN 1090-1)", key="check_1090")


# =========================================================
# 3. LOGICA DI GENERAZIONE (MOTORE DI CALCOLO)
# =========================================================
st.divider()

if st.button("🚀 GENERA STRINGA FINALE", use_container_width=True):
    if 'articolo_scelto' in locals() and articolo_scelto:
        
        articoli_macro = DATABASE.get(macro_selezionata, {}).get("Articoli", {})
        dati_art = articoli_macro.get(articolo_scelto, {})
        
        output_tech_base = dati_art.get("output_tech", articolo_scelto.upper())
        output_comm_base = dati_art.get("output_comm", articolo_scelto.upper())
        ha_finitura = dati_art.get("ha_finitura", False)
        
        finitura_tech_str = ""
        finitura_comm_str = ""
        
        if ha_finitura:
            fin_scelta_ui = st.session_state.get("select_finitura", "")
            tuple_fin = FINITURE_CONFIG.get(fin_scelta_ui, ("", ""))
            if isinstance(tuple_fin, (tuple, list)) and len(tuple_fin) >= 2:
                finitura_tech_str = str(tuple_fin[0]).strip().upper()
                finitura_comm_str = str(tuple_fin[1]).strip().upper()
            else:
                finitura_tech_str = str(fin_scelta_ui).strip().upper()
                finitura_comm_str = finitura_tech_str

        dim_list = []
        L = str(st.session_state.get("dim_l", "") or "").strip()
        P = str(st.session_state.get("dim_p", "") or "").strip()
        H = str(st.session_state.get("dim_h", "") or "").strip()
        D = str(st.session_state.get("dim_dia", "") or "").strip()
        S = str(st.session_state.get("dim_s", "") or "").strip()

        if L: dim_list.append(f"L{L.upper()}")
        if P: dim_list.append(f"P{P.upper()}")
        if H: dim_list.append(f"H{H.upper()}")
        if D: dim_list.append(f"Ø{D.upper()}")
        if S:
            s_clean = S.upper().replace(".", "").strip()
            s_val = s_clean if s_clean.startswith("SP") else f"SP {s_clean}"
            dim_list.append(s_val)
            
        dim_str = " ".join(dim_list)

        pills_config_art = dati_art.get("pills_config", {})
        tags_selezionati_utente = st.session_state.get('extra_tags', [])
        
        pills_ordinati_utente = sorted(
            tags_selezionati_utente,
            key=lambda t: pills_config_art.get(t, {}).get("ordine", 99)
        )
        
        lista_tech_pills = []
        lista_comm_pills = []
        
        for pill in pills_ordinati_utente:
            if pill in SUB_OPTIONS_CONFIG or f"{pill} (+)" in SUB_OPTIONS_CONFIG:
                key_sub = pill if pill in SUB_OPTIONS_CONFIG else f"{pill} (+)"
                config_sub = SUB_OPTIONS_CONFIG[key_sub]
                
                if "Compatibilità piede di base" in pill:
                    scelta_alt = st.session_state.get(f"dyn_alt_{pill}", "")
                    scelta_lung = st.session_state.get(f"dyn_lung_{pill}", "")
                    
                    h_num = str(scelta_alt).replace("H", "").strip() if scelta_alt else ""
                    l_num = str(scelta_lung).replace("L", "").strip() if scelta_lung else ""
                    
                    piede_parts = []
                    if h_num: piede_parts.append(h_num)
                    if l_num: piede_parts.append(f"L{l_num}")
                    
                    if piede_parts:
                        res_piede = f"XP{''.join(piede_parts)}"
                        lista_tech_pills.append(res_piede)
                        lista_comm_pills.append(res_piede)
                else:
                    scelta_utente = st.session_state.get(f"dyn_val_{pill}", "")
                    valore_mappato = config_sub.get(scelta_utente, ("", ""))
                    
                    if isinstance(valore_mappato, (tuple, list)) and len(valore_mappato) >= 2:
                        t_val = str(valore_mappato[0]).strip().upper()
                        c_val = str(valore_mappato[1]).strip().upper()
                    else:
                        t_val = str(valore_mappato).strip().upper()
                        c_val = t_val
                        
                    if t_val: lista_tech_pills.append(t_val)
                    if c_val: lista_comm_pills.append(c_val)
            else:
                tuple_pill = DATABASE_PILLS.get(pill, (pill.upper(), pill.upper()))
                if isinstance(tuple_pill, (tuple, list)) and len(tuple_pill) >= 2:
                    t_pill = str(tuple_pill[0]).strip().upper()
                    c_pill = str(tuple_pill[1]).strip().upper()
                else:
                    t_pill = str(tuple_pill).strip().upper()
                    c_pill = t_pill
                    
                if t_pill: lista_tech_pills.append(t_pill)
                if c_pill and c_pill != "NONE": lista_comm_pills.append(c_pill)

        note_libere = str(st.session_state.get("extra_text", "") or "").strip().upper()

        # Assemblaggio Stringa Tecnica
        pezzi_tech = [output_tech_base, finitura_tech_str] + lista_tech_pills
        if dim_str: pezzi_tech.append(dim_str)
        if note_libere: pezzi_tech.append(note_libere)
        if st.session_state.get("check_1090"):
            pezzi_tech.append("(UNI EN 1090-1)")
            
        stringa_tecnica_definitiva = " ".join([p for p in pezzi_tech if p]).upper()

        # Assemblaggio Stringa Commerciale
        pezzi_comm = [output_comm_base, finitura_comm_str] + lista_comm_pills
        if dim_str: pezzi_comm.append(dim_str)
        if note_libere: pezzi_comm.append(note_libere)
        
        stringa_commerciale_definitiva = " ".join([p for p in pezzi_comm if p]).upper()

        st.session_state['stringa_tecnica'] = stringa_tecnica_definitiva
        st.session_state['stringa_commerciale'] = stringa_commerciale_definitiva
        st.session_state['generazione_effettuata'] = True


# =========================================================
# 4. VISUALIZZAZIONE RISULTATI (OUTPUT BOX)
# =========================================================
if st.session_state.get('generazione_effettuata', False):
    st.markdown("### 📋 Risultato Generazione")
    
    col_out1, col_out2 = st.columns(2)
    with col_out1:
        st.markdown("**Stringa Tecnica:**")
        st.code(st.session_state.get('stringa_tecnica', ''), language="text")
    with col_out2:
        st.markdown("**Stringa Commerciale:**")
        st.code(st.session_state.get('stringa_commerciale', ''), language="text")
