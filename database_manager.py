import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import datetime
from difflib import SequenceMatcher

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
    return spreadsheet.get_worksheet(0)

def carica_database():
    """Carica il database dal Google Sheet in un DataFrame Pandas (4 colonne)."""
    expected_cols = ["Codice_Identificativo", "Stringa_Tecnica", "Stringa_Commerciale", "Data_Creazione"]
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

def calcola_somiglianza(str1, str2):
    """Calcola la percentuale di somiglianza tra due stringhe (da 0 a 100)."""
    return round(SequenceMatcher(None, str1.strip().upper(), str2.strip().upper()).ratio() * 100, 1)

def verifica_match_db(stringa_tech_generata, soglia_attenzione=85.0):
    """
    Controlla il database calcolando una percentuale di somiglianza.
    Restituisce: (codice_esistente, stato, percentuale)
    Stati possibili: "ESATTO" (100%), "SIMILE" (>= soglia), "NUOVO" (< soglia)
    """
    df = carica_database()
    if df.empty:
        return None, "NUOVO", 0.0
    
    stringa_pulita = str(stringa_tech_generata).strip().upper()
    
    miglior_match = None
    max_percentuale = 0.0
    
    for _, row in df.iterrows():
        db_stringa = str(row['Stringa_Tecnica']).strip().upper()
        perc = calcola_somiglianza(stringa_pulita, db_stringa)
        
        if perc > max_percentuale:
            max_percentuale = perc
            miglior_match = row['Codice_Identificativo']
            
    if max_percentuale == 100.0:
        return miglior_match, "ESATTO", 100.0
    elif max_percentuale >= soglia_attenzione:
        return miglior_match, "SIMILE", max_percentuale
    
    return None, "NUOVO", max_percentuale

def salva_su_excel(codice_id, stringa_tech, stringa_comm):
    """Salvataggio blindato su Google Sheets a 4 colonne."""
    try:
        ws = get_google_sheet_connection()
        data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        nuova_riga = [
            str(codice_id).strip(), 
            str(stringa_tech).strip().upper(), 
            str(stringa_comm).strip().upper(), 
            data_ora
        ]
        
        try:
            ws.append_row(nuova_riga, value_input_option="USER_ENTERED")
            return True
        except Exception as api_err:
            if "200" in str(api_err):
                return True
            raise api_err 
            
    except Exception:
        try:
            ws = get_google_sheet_connection()
            data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nuova_riga = [
                str(codice_id).strip(), 
                str(stringa_tech).strip().upper(), 
                str(stringa_comm).strip().upper(), 
            data_ora
            ]
            
            tutti_i_dati = ws.get_all_values()
            prossima_riga = len(tutti_i_dati) + 1
            if prossima_riga < 2:
                prossima_riga = 2 
                
            range_str = f"A{prossima_riga}:D{prossima_riga}"
            ws.update(range_str, [nuova_riga], value_input_option="USER_ENTERED")
            return True
            
        except Exception as e_critico:
            st.error(f"Errore critico definitivo di scrittura su Google Sheets: {e_critico}")
            return False
