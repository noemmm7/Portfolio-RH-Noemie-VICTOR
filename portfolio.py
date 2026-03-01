import streamlit as st
from streamlit_option_menu import option_menu

# 1. Configuration
st.set_page_config(page_title="Noémie VICTOR | Portfolio", layout="wide")

# 2. Navigation
selected = option_menu(
    menu_title=None, 
    options=["À propos", "Compétences", "Parcours", "Chatbot IA"], 
    icons=["house", "tools", "briefcase", "robot"], 
    orientation="horizontal",
    styles={
        "container": {"background-color": "#f8f9fa"},
        "nav-link-selected": {"background-color": "#004687"},
    }
)

# 3. Contenu
if selected == "À propos":
    st.title("Noémie VICTOR")
    st.write("Bienvenue sur mon portfolio RH.")

elif selected == "Compétences":
    st.header("🛠 Mes Compétences")
    st.write("Gestion des effectifs, SIRH, Agilité.")

elif selected == "Parcours":
    st.header("📊 Mon Parcours Académique")
    
    # --- TA TIMELINE (Le code que tu voulais) ---
    st.write("### 📚 Mon Parcours Scolaire")
    
    # ÉTAPE 1 : MASTER
    c1, c2 = st.columns([1, 4])
    with c1: 
        st.markdown("**2026-28**")
    with c2: 
        st.markdown("**Master SIRH (Objectif)**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("↑") 

    # ÉTAPE 2 : L3
    c3, c4 = st.columns([1, 4])
    with c3: 
        st.markdown("**2025-26**")
    with c4: 
        st.markdown("**Licence 3 Gestion, Parcours RH**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("↑")

    # ÉTAPE 3 : DUT
    c5, c6 = st.columns([1, 4])
    with c5: 
        st.markdown("**2022-24**")
    with c6: 
        st.markdown("**DUT Gestion des Entreprises et des Administrations**")
        st.caption("IUT de Sénart-Fontainebleau (UPEC)")

    st.divider()
    st.write("### 🏢 Expérience chez NaTran")
    with st.expander("👉 Détails de mes missions"):
        st.write("- Gestion de l'intérim et pilotage des effectifs.")

elif selected == "Chatbot IA":
    st.header("🤖 Chatbot")
    st.write("Posez-moi vos questions !")
