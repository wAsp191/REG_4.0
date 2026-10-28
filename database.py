# ==============================================================================
# CONFIGURAZIONE GLOBALE FINITURE
# ==============================================================================
# Questa struttura è indipendente dalla macro-categoria e viene caricata
# come opzione globale per tutti gli articoli che prevedono una finitura.
#
# STRUTTURA DEL DIZIONARIO:
#     "Nome Visibile nella UI (Tendina)":
#     "Stringa Tecnica (Output Tech)",
#     "Stringa Commerciale (Output Comm)"
# ==============================================================================

FINITURE_CONFIG = {
    
    # Metalli
    "DECAPATA": ("", ""),
    "ZINCATO": ("ZN", "ZINC"),
    "INOX": ("INOX", "INOX"),
    "INOX S/B": ("INOX S/B", "INOX S/B"),
    "INOX TELA DI LINO": ("INOX T/L", "INOX TELA DI LINO"),
    "ALLUMINIO": ("ALL", "ALLUMINIO"),
    
    # Legno e derivati
    "LAMINATO": ("LAM", "LAMINATO"),
    "NOBILITATO": ("NOB", "NOBILITATO"),
    "TRUCIOLARE": ("TRUC", "TRUCIOLARE"),
    "OSB": ("OSB", "OSB"),
    "HPL": ("HPL", "HPL"),
    
    # Plastiche e polimeri
    "PLX": ("PLX", "PLEXIGLASS"),
    "POLICARBONATO": ("POL/CARB", "POLICARBONATO"),
    "PVC": ("PVC", "PVC"),
    "GOMMA": ("GOMMA", "GOMMA"),
    
    # Vetri
    "VETRO TEMPERATO": ("VETR.TEMP", "VETRO TEMPRATO"),
    "VETRO SATINATO": ("VETR.SAT", "VETRO SATINATO")
}
