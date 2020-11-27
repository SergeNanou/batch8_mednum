from pathlib import Path

hard_reset = False
data_path = Path("../data")

if not data_path.exists():
    data_path = Path("./data")

interim_data = data_path / "interim/"
processed_data = data_path / "processed/"
cache_dir = interim_data

INDICE = "GLOBAL COMPETENCES"


CATEGORIES_INT_NUM = {
    "TX_POVERTY": {
        "nom": "Taux de pauvreté",
        "desc": """Proportion des ménages dont les revenus sont inférieurs à 60% du revenu médian""",
    },
    "COUVERTURE_MOBILE": {
        "nom": "Couverture mobile",
        "desc": """Proportion du territoire d'où l'on peut accéder à un réseau de téléphonie mobile""",
    },
    "COUVERTURE_HD_THD": {
        "nom": "Taux de couverture HD / THD",
        "desc": """Proportion des bâtiments reliés à internet Haut Débit ou Très Haut Débit""",
    },
    "nom": "Accès aux interfaces numériques",
    "desc": "Identification des territoires mal couverts par les réseaux ou dans lesquels des populations auront des difficultésfinancières à y accéder ou à s'équiper en terminaux numériques",
}


CATEGORIES_X_INFOS = {
    "nom": "Accès à l'information",
    "desc": "Identification des populations parmi lesquelles s’observent des difficultés à accomplir des démarches administratives",
    "TX_MENSEUL": {
        "nom": "Part des ménages d'une personne",
        "desc": """Proportion des personnes qui vivent seules parmi l'ensemble des ménages""",
    },
    "TX_FAMMONO": {
        "nom": "Part des ménages monoparentaux",
        "desc": "Propoartion des personnes vivant seules avec enfants parmi l'ensemble des ménages",
    },
}

CATEGORIES_X_COMP_ADMIN = {
    "TX_TOT_0A24": {
        "nom": "Part des moins de 25 ans",
        "desc": """Proportion de jeunes de moins de 25 ans dans la population du territoire""",
    },
    "TX_RSA": {
        "nom": "Part des bénéficiaires de minimas sociaux",
        "desc": "Proportion des personnes qui percoivent des aides sociales (RSA, AAH, ASPA,...) parmi la population du territoire",
    },
    "TX_DEMANDEURS_EMPLOI": {
        "nom": "Part des chômeurs (15-64 ans)",
        "desc": "Proportion de personnes en recherche d'emploi et n'ayant pas travaillé récemment parmi la population en âge de travailler du territoire",
    },
    "nom": "Compétences adminitratives",
    "desc": "Identification des populations parmi lesquelles s’observent des difficultés à accomplir des démarches administratives",
}

CATEGORIES_X_COMP_USAGE = {
    "nom": "Compétences usages numériques",
    "desc": "Identification des populations parmi lesquelles s’observe une fréquence d’illectronisme ou difficulté à utiliser internet",
    "TX_65ETPLUS": {
        "nom": "Part des personnes âgés de plus de 65 ans",
        "desc": """Proportion des personnes âgées de plus de 65 ans dans la population du territoire""",
    },
    "TX_NSCOL15P": {
        "nom": "Part des personnes pas/peu diplômés de 15 ans et plus",
        "desc": "Proportion des personnes sans diplôme ou avec des diplôme de niveau inférieur au baccalauréat parmi la population du territoire âgée de plus de 15 ans",
    },
}

TOUT = {
    "nom": "Tous",
    "desc": "Sélections de l'ensemble des indicateurs",
}

TREEVIEW_CHECK_BOX = {
    "tout_axes": TOUT,
    "interfaces_num": CATEGORIES_INT_NUM,
    "infos_num": CATEGORIES_X_INFOS,
    "comp_admin": CATEGORIES_X_COMP_ADMIN,
    "comp_usage_num": CATEGORIES_X_COMP_USAGE,
}
