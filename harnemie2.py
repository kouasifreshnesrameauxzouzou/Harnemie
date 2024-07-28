import streamlit as st
import pandas as pd

# Fonction pour calculer l'indice de risque d'anémie
def calculate_anemia_risk(data):
    risk = 0
    if data['Hb'] < 12:
        risk += 1
    if data['VGM'] < 80:
        risk += 1
    if data['Ferritine'] < 24:
        risk += 1
    if data['Vitamine B12'] < 200:
        risk += 1
    return risk

# Appliquer des styles de couleur et arrière-plan
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #1a1a1a;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>input, .stNumberInput>div>input, .stSelectbox>div>div>div>div {
        background-color: #333333;
        border-radius: 5px;
        padding: 5px;
        border: 1px solid #ccc;
        color: #ffffff;
    }
    .stTextInput>div>input:focus, .stNumberInput>div>input:focus, .stSelectbox>div>div>div>div:focus {
        border-color: #4CAF50;
        outline: none;
    }
    .header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre de l'application
st.title("Détection de l'Anémie")

# Barre latérale pour les menus déroulants
with st.sidebar:
    st.markdown('<div class="header">Informations du Patient</div>', unsafe_allow_html=True)
    patient_name = st.text_input("Nom du Patient")

    st.markdown('<div class="header">Indices Cliniques</div>', unsafe_allow_html=True)
    fatigue = st.selectbox("Fatigue", ["Non", "Oui"])
    paleur = st.selectbox("Pâleur", ["Non", "Oui"])
    essoufflement = st.selectbox("Essoufflement", ["Non", "Oui"])
    palpitations = st.selectbox("Palpitations", ["Non", "Oui"])
    vertiges = st.selectbox("Vertiges et étourdissements", ["Non", "Oui"])
    maux_de_tete = st.selectbox("Maux de tête", ["Non", "Oui"])

    st.markdown('<div class="header">Indices Hématologiques</div>', unsafe_allow_html=True)
    hb = st.number_input("Hémoglobine (g/dL)", min_value=0.0, max_value=20.0, step=0.1)
    vgm = st.number_input("Volume Globulaire Moyen (fl)", min_value=0.0, max_value=150.0, step=0.1)
    ferritine = st.number_input("Ferritine Sérique (ng/mL)", min_value=0.0, max_value=1000.0, step=1.0)
    fer_serique = st.number_input("Fer Sérique (µg/dL)", min_value=0.0, max_value=500.0, step=1.0)
    tibc = st.number_input("Capacité Totale de Liaison du Fer (TIBC) (µg/dL)", min_value=0.0, max_value=600.0, step=1.0)
    transferrine = st.number_input("Saturation de la Transferrine (%)", min_value=0.0, max_value=100.0, step=1.0)

    st.markdown('<div class="header">Indices Biochimiques</div>', unsafe_allow_html=True)
    vit_b12 = st.number_input("Vitamine B12 (pg/mL)", min_value=0.0, max_value=2000.0, step=1.0)
    folate = st.number_input("Folate (ng/mL)", min_value=0.0, max_value=20.0, step=0.1)
    acide_lactique = st.number_input("Acide Lactique (mmol/L)", min_value=0.0, max_value=10.0, step=0.1)
    bilirubine = st.number_input("Bilirubine (mg/dL)", min_value=0.0, max_value=10.0, step=0.1)

    st.markdown('<div class="header">Indices Génétiques et Immunologiques</div>', unsafe_allow_html=True)
    thalassemie = st.selectbox("Thalassémie", ["Non", "Oui"])
    drepanocytose = st.selectbox("Drépanocytose", ["Non", "Oui"])
    test_coombs = st.selectbox("Test de Coombs", ["Non", "Oui"])

# Collecte des données
data = {
    'Nom du Patient': patient_name,
    'Fatigue': fatigue,
    'Pâleur': paleur,
    'Essoufflement': essoufflement,
    'Palpitations': palpitations,
    'Vertiges': vertiges,
    'Maux de tête': maux_de_tete,
    'Hb': hb,
    'VGM': vgm,
    'Ferritine': ferritine,
    'Fer Sérique': fer_serique,
    'TIBC': tibc,
    'Transferrine': transferrine,
    'Vitamine B12': vit_b12,
    'Folate': folate,
    'Acide Lactique': acide_lactique,
    'Bilirubine': bilirubine,
    'Thalassémie': thalassemie,
    'Drépanocytose': drepanocytose,
    'Test de Coombs': test_coombs
}

# Bouton pour soumettre les données
if st.button("Évaluer le risque d'anémie"):
    if patient_name.strip() == "":
        st.warning("Veuillez entrer le nom du patient.")
    else:
        risk = calculate_anemia_risk(data)
        if risk > 1:
            st.error("Risque élevé d'anémie pour " + patient_name)
        else:
            st.success("Risque faible d'anémie pour " + patient_name)

# Affichage des résultats sous forme de graphique
st.markdown('<div class="header">Résultats</div>', unsafe_allow_html=True)
if st.checkbox("Afficher les données sous forme de tableau"):
    st.dataframe(pd.DataFrame([data]))

st.markdown('<div class="header">Graphiques des Indicateurs</div>', unsafe_allow_html=True)
st.bar_chart(pd.DataFrame(data, index=[0]).drop(columns=["Nom du Patient"]))

