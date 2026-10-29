import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import datetime

def get_google_sheet_connection():
    """Connessione sicura e blindata a Google Sheets tramite st.secrets."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_dict = dict(st.secrets["gcp_service_account"])
    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
    client = gspread.authorize(creds)
    
    sheet_name = st.secrets["sheet_config"]["sheet_name"]
    spreadsheet = client.open(sheet_name)
    
    # Seleziona in modo sicuro il primo foglio disponibile
    return spreadsheet.get_worksheet(0)

def carica_database():
    """Carica il database dal Google Sheet in un DataFrame Pandas in modo sicuro."""
    expected_cols = ["Codice_Identificativo", "Stringa_Tecnica", "Stringa_Commerciale", "Data_Creazione", "Utente"]
    try:
        ws = get_google_sheet_connection()
        data = ws.get_all_records()
        
        if not data:
            return pd.DataFrame(columns=expected_cols)
            
        df = pd.DataFrame(data)
        if df.empty or not all(col in df.columns for col in expected_cols):
            return pd.DataFrame(columns=expected_cols)
        return df
    except Exception:
        return pd.DataFrame(columns=expected_cols)

def verifica_match_db(stringa_tech_generata):
    """Controlla se la stringa tecnica generata esiste già nel Google Sheet."""
    df = carica_database()
    if df.empty:
        return None, "NUOVO"
    
    stringa_pulita = str(stringa_tech_generata).strip().upper()
    df['Tech_Clean'] = df['Stringa_Tecnica'].astype(str).str.strip().str.upper()
    
    match = df[df['Tech_Clean'] == stringa_pulita]
    if not match.empty:
        codice_esistente = match.iloc[0]['Codice_Identificativo']
        return codice_esistente, "ESATTO"
    
    return None, "NUOVO"

def salva_su_excel(codice_id, stringa_tech, stringa_comm, utente="Anonimo"):
    """Aggiunge una nuova riga nel Google Sheet con diagnostica avanzata dell'errore."""
    try:
        ws = get_google_sheet_connection()
        data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        nuova_riga = [
            str(codice_id).strip(), 
            str(stringa_tech).strip().upper(), 
            str(stringa_comm).strip().upper(), 
            data_ora,
            str(utente).strip()
        ]
        
        # Eseguiamo l'append
        ws.append_row(nuova_riga, value_input_option="USER_ENTERED")
        return True
        
    except Exception as e:
        # Estraiamo il testo dettagliato della risposta HTTP di Google se disponibile
        error_details = str(e)
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            error_details += f" | Contenuto risposta Google: {e.response.text}"
            
        st.error(f"🔍 Debug Errore Google Sheets: {error_details}")
        return False
