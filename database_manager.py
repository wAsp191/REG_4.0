import os
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import datetime

EXCEL_DB_PATH = "database_esempi.xlsx"

def inizializza_excel_db():
    """Crea il file Excel di database con intestazioni e formattazione professionale se non esiste."""
    if not os.path.exists(EXCEL_DB_PATH):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Database_Stringhe"
        
        # Intestazioni
        intestazioni = ["Codice_Identificativo", "Stringa_Tecnica", "Stringa_Commerciale", "Data_Creazione"]
        ws.append(intestazioni)
        
        # Stili di formattazione professionale
        header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid") # Blu professionale
        header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        thin_border = Border(
            left=Side(style='thin', color='D9D9D9'),
            right=Side(style='thin', color='D9D9D9'),
            top=Side(style='thin', color='D9D9D9'),
            bottom=Side(style='thin', color='D9D9D9')
        )
        
        # Formattazione della riga di intestazione
        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center")
            
        # Imposta un'altezza comoda per l'intestazione
        ws.row_dimensions[1].height = 25
        
        wb.save(EXCEL_DB_PATH)

def carica_database():
    """Carica il database Excel in un DataFrame Pandas in modo sicuro."""
    inizializza_excel_db()
    try:
        df = pd.read_excel(EXCEL_DB_PATH)
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
    """
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

def salva_su_excel(codice_id, stringa_tech, stringa_comm):
    """Aggiunge una nuova riga formattata correttamente nel file Excel."""
    inizializza_excel_db()
    
    wb = openpyxl.load_workbook(EXCEL_DB_PATH)
    ws = wb.active
    data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nuova_riga = [
        str(codice_id).strip(), 
        str(stringa_tech).strip().upper(), 
        str(stringa_comm).strip().upper(), 
        data_ora
    ]
    ws.append(nuova_riga)
    
    # Applica i bordi e l'allineamento anche alla nuova riga appena inserita
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )
    
    row_idx = ws.max_row
    ws.row_dimensions[row_idx].height = 20
    for col_idx in range(1, len(nuova_riga) + 1):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center")
        if col_idx in [1, 4]:  # Centriamo ID e Data
            cell.alignment = Alignment(horizontal="center", vertical="center")

    # Autofit larghezza colonne dinamico
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 15)

    wb.save(EXCEL_DB_PATH)
