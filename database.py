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

# ==============================================================================
# DATABASE ARTICOLI: SALES PART
# ==============================================================================

SALES_PART_ARTICOLI = {
    "Adattatore": {
        "output_tech": "ADATTATORE",
        "output_comm": "ADATTATORE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Anta": {
        "output_tech": "ANTA",
        "output_comm": "ANTA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Canalina passa cavi": {
        "output_tech": "CANALINA_PASSA_CAVI",
        "output_comm": "CANALINA PASSA CAVI",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Cesto in filo": {
        "output_tech": "CESTO_FILO",
        "output_comm": "CESTO IN FILO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Chiusura": {
        "output_tech": "CHIUSURA",
        "output_comm": "CHIUSURA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Cielino": {
        "output_tech": "CIELINO",
        "output_comm": "CIELINO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Compensazione": {
        "output_tech": "COMPENSAZIONE",
        "output_comm": "COMPENSAZIONE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Coprimontante": {
        "output_tech": "COPRIMONTANTE",
        "output_comm": "COPRIMONTANTE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Copripiede": {
        "output_tech": "COPRIPIEDE",
        "output_comm": "COPRIPIEDE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Coprischienale": {
        "output_tech": "COPRISCHIENALE",
        "output_comm": "COPRISCHIENALE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Corrente": {
        "output_tech": "CORRENTE",
        "output_comm": "CORRENTE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Diagonale": {
        "output_tech": "DIAGONALE",
        "output_comm": "DIAGONALE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Distanziale": {
        "output_tech": "DISTANZIALE",
        "output_comm": "DISTANZIALE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Divisorio": {
        "output_tech": "DIVISORIO",
        "output_comm": "DIVISORIO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Fiancata laterale": {
        "output_tech": "FIANCATA_LATERALE",
        "output_comm": "FIANCATA LATERALE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Filo": {
        "output_tech": "FILO",
        "output_comm": "FILO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Frontalino": {
        "output_tech": "FRONTALINO",
        "output_comm": "FRONTALINO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Frontale": {
        "output_tech": "FRONTALE",
        "output_comm": "FRONTALE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Gancio": {
        "output_tech": "GANCIO",
        "output_comm": "GANCIO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Mensola": {
        "output_tech": "MENSOLA",
        "output_comm": "MENSOLA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Montante": {
        "output_tech": "MONTANTE",
        "output_comm": "MONTANTE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Pannello": {
        "output_tech": "PANNELLO",
        "output_comm": "PANNELLO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Pannello di rivestimento": {
        "output_tech": "PANNELLO_RIVESTIMENTO",
        "output_comm": "PANNELLO RIVESTIMENTO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Pannello frontale": {
        "output_tech": "PANNELLO_FRONTALE",
        "output_comm": "PANNELLO FRONTALE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Pedana di base": {
        "output_tech": "PEDANA_BASE",
        "output_comm": "PEDANA DI BASE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Piastra di fissaggio": {
        "output_tech": "PIASTRA_FISSAGGIO",
        "output_comm": "PIASTRA FISSAGGIO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Piede di base": {
        "output_tech": "PIEDE_BASE",
        "output_comm": "PIEDE DI BASE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Profilo": {
        "output_tech": "PROFILO",
        "output_comm": "PROFILO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Protezione": {
        "output_tech": "PROTEZIONE",
        "output_comm": "PROTEZIONE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Rinforzo": {
        "output_tech": "RINFORZO",
        "output_comm": "RINFORZO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Ripiano": {
        "output_tech": "RIPIANO",
        "output_comm": "RIPIANO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Schienale": {
        "output_tech": "SCHIENALE",
        "output_comm": "SCHIENALE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Staffa": {
        "output_tech": "STAFFA",
        "output_comm": "STAFFA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Tamponamento": {
        "output_tech": "TAMPONAMENTO",
        "output_comm": "TAMPONAMENTO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Tappo": {
        "output_tech": "TAPPO",
        "output_comm": "TAPPO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Traversino": {
        "output_tech": "TRAVERSINO",
        "output_comm": "TRAVERSINO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Tubolare": {
        "output_tech": "TUBOLARE",
        "output_comm": "TUBOLARE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Vasca": {
        "output_tech": "VASCA",
        "output_comm": "VASCA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Zoccolatura": {
        "output_tech": "ZOCCOLATURA",
        "output_comm": "ZOCCOLATURA",
        "ha_finitura": True,
        "pills_config": {}
    }
}

# ==============================================================================
# DATABASE ARTICOLI: PACKAGE PART (Solo quelli specifici)
# ==============================================================================

PACKAGE_PART_SPECIFICI = {
    "Avancassa": {
        "output_tech": "AVANCASSA",
        "output_comm": "AVANCASSA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Banco espositore": {
        "output_tech": "BANCO_ESPOSITORE",
        "output_comm": "BANCO ESPOSITORE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Cancelletto": {
        "output_tech": "CANCELLETTO",
        "output_comm": "CANCELLETTO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Cassa pagamento automatico": {
        "output_tech": "CASSA_PAGAMENTO_AUTOMATICO",
        "output_comm": "CASSA PAGAMENTO AUTOMATICO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Cassetto estraibile": {
        "output_tech": "CASSETTO_ESTRAIBILE",
        "output_comm": "CASSETTO ESTRAIBILE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Cassettiera": {
        "output_tech": "CASSETTIERA",
        "output_comm": "CASSETTIERA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Controventatura": {
        "output_tech": "CONTROVENTATURA",
        "output_comm": "CONTROVENTATURA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Espositore": {
        "output_tech": "ESPOSITORE",
        "output_comm": "ESPOSITORE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Espositore a gradoni": {
        "output_tech": "ESPOSITORE_GRADONI",
        "output_comm": "ESPOSITORE A GRADONI",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Espositore riviste": {
        "output_tech": "ESPOSITORE_RIVISTE",
        "output_comm": "ESPOSITORE RIVISTE",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Spalla": {
        "output_tech": "SPALLA",
        "output_comm": "SPALLA",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Telaio saldato": {
        "output_tech": "TELAIO_SALDATO",
        "output_comm": "TELAIO SALDATO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Totem": {
        "output_tech": "TOTEM",
        "output_comm": "TOTEM",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Vetrina": {
        "output_tech": "VETRINA",
        "output_comm": "VETRINA",
        "ha_finitura": True,
        "pills_config": {}
    }
}

# ==============================================================================
# DATABASE ARTICOLI: LEGNO
# ==============================================================================

LEGNO_ARTICOLI = {
    "Anta": {
        "output_tech": "ANTA_LEGNO",
        "output_comm": "ANTA IN LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Asta in legno": {
        "output_tech": "ASTA_LEGNO",
        "output_comm": "ASTA IN LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Cielino": {
        "output_tech": "CIELINO_LEGNO",
        "output_comm": "CIELINO LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Compensazione": {
        "output_tech": "COMPENSAZIONE_LEGNO",
        "output_comm": "COMPENSAZIONE LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Copripiede": {
        "output_tech": "COPRIPIEDE_LEGNO",
        "output_comm": "COPRIPIEDE LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Coprimontante": {
        "output_tech": "COPRIMONTANTE_LEGNO",
        "output_comm": "COPRIMONTANTE LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Coprischienale": {
        "output_tech": "COPRISCHIENALE_LEGNO",
        "output_comm": "COPRISCHIENALE LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Fiancata laterale": {
        "output_tech": "FIANCATA_LATERALE_LEGNO",
        "output_comm": "FIANCATA LATERALE LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Pannello": {
        "output_tech": "PANNELLO_LEGNO",
        "output_comm": "PANNELLO LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Ripiano": {
        "output_tech": "RIPIANO_LEGNO",
        "output_comm": "RIPIANO LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Schienale": {
        "output_tech": "SCHIENALE_LEGNO",
        "output_comm": "SCHIENALE LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Tamponamento": {
        "output_tech": "TAMPONAMENTO_LEGNO",
        "output_comm": "TAMPONAMENTO LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    },
    "Zoccolatura": {
        "output_tech": "ZOCCOLATURA_LEGNO",
        "output_comm": "ZOCCOLATURA LEGNO",
        "ha_finitura": True,
        "pills_config": {}
    }
}

# ==============================================================================
# MASTER DATABASE ARTICOLI
# ==============================================================================

DATABASE = {
    "SALES PART": {
        "macro_name": "SALES PART",
        "Articoli": SALES_PART_ARTICOLI
    },
    
    "PACKAGE PART": {
        "macro_name": "PACKAGE PART",
        # Unisce automaticamente tutti i Sales Part + i Package Part specifici
        "Articoli": SALES_PART_ARTICOLI | PACKAGE_PART_SPECIFICI
    },
    
    "LEGNO": {
        "macro_name": "LEGNO",
        "Articoli": LEGNO_ARTICOLI
    }
}
