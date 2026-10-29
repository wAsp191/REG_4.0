# ==============================================================================
# CONFIGURAZIONE GLOBALE FINITURE
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

OPZIONI_COMPATIBILITA = ["", "F25", "F25 BESPOKE", "F50", "F50 BESPOKE", "UNIVERSAL", "BC", "FORTISSIMO", "MINIRACK", "UNIMOB"]

# ==============================================================================
# DATABASE ARTICOLI: SALES PART
# ==============================================================================
SALES_PART_ARTICOLI = {
    "Adattatore": {
        "output_tech": "ADATT",
        "output_comm": "ADATTATORE",
        "ha_finitura": True,
        "pills_config": [
            ("Antisgancio", 5),
            ("Attacco montante", 6),
            ("Compatibilità piede di base (+)", 4),
            ("Con componente saldato", 7),
            ("Con inserti filettati", 8),
            ("Con viteria", 9),
            ("Forato", 2),
            ("Liscio", 10),
            ("Orientamento Destro / Sinistro (+)", 1),
            ("Predisposto per montante (+)", 11),
            ("Per ripiano di base", 12),
            ("Per ripiano di legno", 13),
            ("Per ripiano di vetro", 14),
            ("Piegato", 15),
            ("Regolabile", 3)
        ]
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
        "output_tech": "PANN RIV",
        "output_comm": "PANNELLO RIVESTIMENTO",
        "ha_finitura": True,
        "pills_config": [
            ("Antisgancio", 6),
            ("Attacco montante", 5),
            ("Con componente saldato", 7),
            ("Con viteria", 9),
            ("Forato", 4),
            ("Liscio", 3),
            ("Orientamento Destro / Sinistro (+)", 1),
            ("Predisposto per montante (+)", 8),
            ("Con finestra", 9),
            ("Angolo aperto", 10),
            ("Angolo chiuso", 11),
            ("Con scasso", 12),
            ("Scantonato", 2)
        ]
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
        "Articoli": SALES_PART_ARTICOLI | PACKAGE_PART_SPECIFICI
    },
    "LEGNO": {
        "macro_name": "LEGNO",
        "Articoli": LEGNO_ARTICOLI
    }
}
# ==============================================================================
# DATABASE PILLS (SEMPLICI)
# ==============================================================================
DATABASE_PILLS = {
    "Angolo aperto": ("ANG AP", "ANGOLO APERTO"),
    "Angolo chiuso": ("ANG CHI", "ANGOLO CHIUSO"),
    "Antisgancio": ("ANT-SGANCIO", "ANTISGANCIO"),
    "Antisismico": ("ANT-SISM", "ANTISISMICO"),
    "Antiurto": ("ANT-URT", "ANTIURTO"),
    "Asolato": ("ASOL", "ASOLATO"),
    "Asolata": ("ASOL", "ASOLATA"),
    "Attacco a pinza": ("ATT PINZ", "ATTACCO A PINZA"),
    "Attacco a seggiola": ("ATT SEGG", "ATTACCO A SEGGIOLA"),
    "Attacco montante": ("ATT MONT", "ATTACCO MONTANTE"),
    "Biasolato": ("BI-ASOL", "BIASOLATO"),
    "Bordi smussati": ("B. SMUSS", "BORDI SMUSSATI"),
    "Completa di paracolpo ABS": ("CON PAR. ABS", "COMPLETA DI PARACOLPO ABS"),
    "Con ante scorrevoli": ("CON ANTE SCORR", "CON ANTE SCORREVOLI"),
    "Con batticarrello": ("CON BATT-CARRELLO", "CON BATTCARRELLO"),
    "Con bocchetta passacavi": ("CON BOCC P.CAVI", "CON BOCCHETTA PASSACAVI"),
    "Con collegamento superiore": ("CON COLL SUP", "CON COLLEGAMENTO SUPERIORE"),
    "Con compensazioni removibili": ("CON COMP REM", "CON COMPENSAZIONI REMOVIBILI"),
    "Con componente saldato": ("SALD", "CON COMPONENTE SALDATO"),
    "Con finestra": ("CON FIN", "CON FINESTRA"),
    "Con foro serratura": ("CON FOR SERR", "CON FORO SERRATURA"),
    "Con guide RAM": ("+ G. RAM", "CON GUIDE RAM"),
    "Con illuminazione": ("CON ILLUM", "CON ILLUMINAZIONE"),
    "Con inserti filettati": ("+BOCC", "CON INSERTI FILETTATI"),
    "Con lati bordati": ("BORD", "CON LATI BORDATI"),
    "Con macchine di pagamento": ("CON MACCHINE DI PAGAMENTO", "CON MACCHINE DI PAGAMENTO"),
    "Con mensole": ("CON MENS", "CON MENSOLE"),
    "Con mensole saldate": ("CON MENS SALD", "CON MENSOLE SALDATE"),
    "Con portaprezzo": ("+PPRZ", "CON PORTAPREZZO"),
    "Con rinforzo": ("R", "CON RINFORZO/I"),
    "Con ripiani": ("CON RIP", "CON RIPIANI"),
    "Con ripiani inclinati": ("CON RIP INCL", "CON RIPIANI INCLINATI"),
    "Con ruote": ("+RUOTE", "CON RUOTE"),
    "Con scasso": ("SCASS", "CON SCASSO"),
    "Con scritta": ("CON SCRITTA", "CON SCRITTA"),
    "Con serratura": ("+SERR", "CON SERRATURA"),
    "Con viteria": ("+VIT", "CON VITERIA"),
    "Con viteria saldata": ("+VIT SALD", "CON VITERIA SALDATA"),
    "Dritto": ("DRITT", "DRITTO"),
    "Forato": ("FOR", "FORATO"),
    "Forata": ("FOR", "FORATA"),
    "Fresata": ("FRES", "FRESATA"),
    "Fresato": ("FRES", "FRESATO"),
    "Impilabile": ("IMP", "IMPILABILE"),
    "In filo": ("IN FILO", "IN FILO"),
    "In rete": ("IN RETE", "IN RETE"),
    "Inclinato": ("INCL", "INCLINATO"),
    "Inclinata": ("INCL", "INCLINATA"),
    "Liscio": ("LISC", "LISCIO"),
    "Liscia": ("LISC", "LISCIA"),
    "Mobile": ("MOB", "MOBILE"),
    "Nervata": ("NERV", "NERVATA"),
    "Per piani cottura": ("X PIANI COTT", "PER PIANI COTTURA"),
    "Per ripiano di base": ("X RIP BAS", "PER RIPIANO DI BASE"),
    "Per ripiano in legno": ("X RIP LEGNO", "PER RIPIANO IN LEGNO"),
    "Per ripiano in vetro": ("X RIP VETR", "PER RIPIANO IN VETRO"),
    "Piegato": ("PIEG", "PIEGATO"),
    "Piegata": ("PIEG", "PIEGATA"),
    "Portante": ("PORT", "PORTANTE"),
    "Predisposta per guida RAM": ("PRED G. RAM", "PREDISPOSTA PER GUIDA RAM"),
    "Profilo a L": ("PROF L", "PROFILO A L"),
    "Profilo a U": ("PROF U", "PROFILO A U"),
    "Rasterizzato": ("RAST", "RASTERIZZATO"),
    "Rasterizzata": ("RAST", "RASTERIZZATA"),
    "Regolabile": ("REG", "REGOLABILE"),
    "Rotante": ("ROTANTE", "ROT"),
    "Scantonato": ("SCANT", "SCANTONATO"),
    "Scantonata": ("SCANT", "SCANTONATA"),
    "Scorrevole": ("SCORR", "SCORREVOLE"),
    "Statico": ("STAT", "STATICO"),
    "Stondato": ("STOND", "STONDATO"),
    "Stondata": ("STOND", "STONDATA"),
    "Verniciato": ("VERN", "VERNICIATO"),
    "Verniciata": ("VERN", "VERNICIATA"),
    "Zincato": ("ZN", "ZINC"),
}
# ==============================================================================
# CONFIGURAZIONE SUB-OPTIONS / PILLS MULTISCELTA (+)
# ==============================================================================
SUB_OPTIONS_CONFIG = {
    "VPA (+)": {
        "Serie S": ("VPA S", "VPA S"),
        "Serie SS": ("VPA SS", "VPA SS"),
        "Serie M": ("VPA M", "VPA M"),
        "Serie L": ("VPA L", "VPA L")
    },
    "Con distanziale (+)": {
        "L100": ("S100", "S100"),
        "L150": ("S150", "S150"),
        "L200": ("S200", "S200"),
        "L250": ("S250", "S250")
    },
    "Numero diagonali (+)": {
        "Doppie": ("DD", "DIAGONALI DOPPIE"),
        "Triple": ("DT", "DIAGONALI TRIPLE"),
        "Quadruple": ("DQ", "DIAGONALI QUADRUPLE")
    },
    "Sezione montante (+)": {
        "L55": ("L55", "L55"),
        "L80 Z/S": ("L80 Z/S", "L80 Z/S"),
        "L80 Z/M": ("L80 Z/M", "L80 Z/M"),
        "L100 Z/S": ("L100 Z/S", "L100 Z/S"),
        "L100 Z/M": ("L100 Z/M", "L100 Z/M"),
        "L120 Z/S": ("L120 Z/S", "L120 Z/S"),
        "70X30": ("70X30", "70X30"),
        "90X30": ("90X30", "90X30"),
        "30X30": ("30X30", "30X30")
    },
    "Tipologia di mensola saldata (+)": {
        "Mensola saldata a filo superiore": ("MENS.FILO SUP", "MENSOLA SALDATA FILO SUPERIORE"),
        "Mensola saldata a filo inferiore": ("MENS.FILO INF", "MENSOLA SALDATA FILO INFERIORE")
    },
    "Compatibilità piede di base (+)": {
        "altezze": {
            "": ("", ""),
            "H90": ("XP90", "90"),
            "H100": ("XP100", "100"),
            "H150": ("XP150", "150")
        },
        "lunghezze": {
            "": ("", ""),
            "L300": ("L300", "L300"),
            "L350": ("L350", "L350"),
            "L400": ("L400", "L400"),
            "L450": ("L450", "L450"),
            "L500": ("L500", "L500"),
            "L550": ("L550", "L550"),
            "L600": ("L600", "L600")
        }
    },
    "Attacco gancio (+)": {
        "Attacco barra": ("ATT BARR", "ATTACCO BARRA"),
        "Attacco multilama": ("ATT M-LAME", "ATTACCO MULTILAMA"),
        "Attacco pannello forato": ("ATT PANN FOR", "ATTACCO PANNELLO FORATO")
    },
    "Orientamento Destro / Sinistro (+)": {
        "Destra": ("DX", "DX"),
        "Sinistra": ("SX", "SX")
    },
    "Posizioni multiple (+)": {
        "2 Posizioni": ("2P", "2 POSIZIONI"),
        "3 Posizioni": ("3P", "3 POSIZIONI")
    },
    "Altezza piede (+)": {
        "H90": ("H90", "H90"),
        "H100": ("H100", "H100"),
        "H150": ("H150", "H150")
    },
    "Predisposto per montante (+)": {
        "L80": ("XML80", "PREDISPOSTO PER MONTANTE L80"),
        "L100/L120": ("XML100/L120", "PREDISPOSTO PER MONTANTE L100/120")
    },
    "Asimmetrica (+)": {
        "AS240": ("AS240", "AS240"),
        "AS340": ("AS340", "AS340"),
        "AS440": ("AS440", "AS440")
    },
    "Lato della fresatura (+)": {
        "DX": ("FRES.DX", "FRESATURA LATO DESTRO"),
        "SX": ("FRES.SX", "FRESATURA LATO SINISTRO"),
        "Centrale": ("FRES.CTR", "FRESATURA CENTRALE")
    }
}
