import streamlit as st
from streamlit_option_menu import option_menu

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Noémie VICTOR | Portfolio", layout="wide")

# 2. FORCE LE FOND BLANC ET LE TEXTE NOIR (Design Pro)
st.markdown("""
    <style>
    /* Fond de l'application */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Force le noir pour tous les textes */
    h1, h2, h3, p, span, div, li, label {
        color: #1A1A1A !important;
    }

    /* Style spécifique pour le menu horizontal */
    .nav-link {
        color: #1A1A1A !important;
    }
    
    /* Bouton de téléchargement bleu */
    .stDownloadButton button {
        background-color: #004687 !important;
        color: white !important;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRE DE NAVIGATION
selected = option_menu(
    menu_title=None, 
    options=["À propos", "Compétences", "Parcours", "Chatbot IA"], 
    icons=["house", "tools", "briefcase", "robot"], 
    orientation="horizontal",
    styles={
        "container": {"background-color": "#f8f9fa", "border": "1px solid #EEEEEE"},
        "nav-link-selected": {"background-color": "#004687", "color": "white"},
    }
)

# 4. CONTENU DES SECTIONS
if selected == "À propos":
    st.title("Noémie VICTOR")
    st.write("Future Product Owner SIRH.")
    st.write("Bienvenue sur mon portfolio en fond blanc pur !")

elif selected == "Compétences":
    st.header("🛠 Mes Compétences")
    # Tes blocs de compétences ici...

elif selected == "Parcours":
    st.header("📊 Mon Parcours Académique")
    
    # ÉTAPE 1 : MASTER
    c1, c2 = st.columns([1, 4])
    with c1: st.markdown("**2026-28**")
    with c2: 
        st.markdown("**Master SIRH (Objectif)**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("↑") 

    # ÉTAPE 2 : L3
    c3, c4 = st.columns([1, 4])
    with c3: st.markdown("**2025-26**")
    with c4: 
        st.markdown("**Licence 3 Gestion, Parcours RH**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("↑")

    # ÉTAPE 3 : DUT
    c5, c6 = st.columns([1, 4])
    with c5: st.markdown("**2022-24**")
    with c6: 
        st.markdown("**DUT Gestion des Entreprises et des Administrations**")
        st.caption("IUT de Sénart-Fontainebleau (UPEC)")

elif selected == "Chatbot IA":
    st.header("🤖 Chatbot")
    st.write("Posez-moi vos questions !")
