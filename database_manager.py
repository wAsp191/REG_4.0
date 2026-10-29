import os
import pandas as pd
import openpyxl
import datetime

EXCEL_DB_PATH = "database_esempi.xlsx"

def inizializza_excel_db():
    """Crea il file Excel di database con le relative intestazioni se non esiste."""
    if not os.path.exists(EXCEL_DB_PATH):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Database_Stringhe"
        ws.append(["Codice_Identificativo", "Stringa_Tecnica", "Stringa_Commerciale", "Data_Creazione"])
        wb.save(EXCEL_DB_PATH)

def carica_database():
    """Carica il database Excel in un DataFrame Pandas in modo sicuro."""
    inizializza_excel_db()
    try:
        df = pd.read_excel(EXCEL_DB_PATH)
        # Assicuriamoci che le colonne essenziali esistano
        expected_cols = ["Codice_Identificativo", "Stringa_Tecnica", "Stringa_Commerciale", "Data_Creazione"]
        if not all(col in df.columns for col in expected_cols):
            return pd.DataFrame(columns=expected_cols)
        return df
    except Exception:
        return pd.DataFrame(columns=["Codice_Identificativo", "Stringa_Tecnica", "Stringa_Commerciale", "Data_Creazione"])

def verifica_match_db(stringa_tech_generata):
    """
    Controlla se la stringa tecnica generata esiste già nel database Excel.
    Ritorna una tupla: (codice_esistente_o_None, stato_match)
    Stati: "ESATTO" oppure "NUOVO"
    """
    df = carica_database()
    if df.empty:
        return None, "NUOVO"
    
    # Normalizziamo per evitare falsi negativi dovuti a spazi o maiuscole/minuscole
    stringa_pulita = str(stringa_tech_generata).strip().upper()
    df['Tech_Clean'] = df['Stringa_Tecnica'].astype(str).str.strip().str.upper()
    
    match = df[df['Tech_Clean'] == stringa_pulita]
    if not match.empty:
        codice_esistente = match.iloc[0]['Codice_Identificativo']
        return codice_esistente, "ESATTO"
    
    return None, "NUOVO"

def salva_su_excel(codice_id, stringa_tech, stringa_comm):
    """Aggiunge una nuova riga con il nuovo codice e le stringhe generate nel file Excel."""
    inizializza_excel_db()
    
    wb = openpyxl.load_workbook(EXCEL_DB_PATH)
    ws = wb.active
    data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ws.append([
        str(codice_id).strip(), 
        str(stringa_tech).strip().upper(), 
        str(stringa_comm).strip().upper(), 
        data_ora
    ])
    wb.save(EXCEL_DB_PATH)
