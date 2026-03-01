import streamlit as st
from streamlit_option_menu import option_menu

if selected == "Accueil":
    # 1. Image de bannière (Style montagne ou bureau)
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80", use_column_width=True)

    # 2. Titre avec style forcé en NOIR pour la visibilité
    st.markdown("""
        <div style="text-align: center; margin-top: -150px; padding-bottom: 100px;">
            <h1 style="color: white; text-shadow: 2px 2px 4px #000000; font-size: 60px;">Noémie VICTOR</h1>
            <h2 style="color: white; text-shadow: 2px 2px 4px #000000;">Étudiante en Gestion des Ressources Humaines</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("##") # Espace pour respirer

    # --- NOUVELLE SECTION : PHOTO + TEXTE CÔTE À CÔTE ---
    # Création de deux colonnes : 1/3 pour la photo, 2/3 pour le texte
    col_photo, col_texte = st.columns([1, 2])
    
    with col_photo:
        # Affiche ta photo (Assure-toi que le fichier est sur GitHub)
        st.image("Photo Noemie.jpg", width=300) 
        
    with col_texte:
        st.write("""
        ### 📍 À propos de moi
        Bienvenue sur mon portfolio interactif !
        
        Actuellement en **Licence 3 RH** à l'Université Paris 1 Panthéon-Sorbonne, 
        je développe mes compétences en alternance chez **NaTran**. 
        
        Passionnée par l'innovation digitale appliquée aux RH, je construis ce projet 
        pour démontrer ma capacité à lier gestion humaine et outils technologiques.
        
        ---
        🎯 **Objectif :** Master SIRH & Product Owner
        """)

elif selected == "Compétences":

# 1. CONFIGURATION
st.set_page_config(page_title="Noémie VICTOR | Portfolio", layout="wide")

# 2. DESIGN GRIS & NOIR (CSS personnalisé)
st.markdown("""
    <style>
    /* Fond de l'application blanc pour le contraste */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Titres et textes en Noir Anthracite */
    h1, h2, h3, p, span, div, label {
        color: #1A1A1A !important;
    }

    /* Boutons et barres de progression en GRIS FONCÉ */
    .stDownloadButton button {
        background-color: #333333 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px;
    }
    
    /* Barres de progression en gris */
    .stProgress > div > div > div > div {
        background-color: #555555 !important;
    }

    /* Style du texte sur l'image d'accueil */
    .hero-text {
        text-align: center;
        margin-top: -260px;
        padding-bottom: 160px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRE DE NAVIGATION (Gris Foncé et Noir)
selected = option_menu(
    menu_title=None, 
    options=["Accueil", "Compétences", "Parcours", "Chatbot IA", "Contact"], 
    icons=["house", "tools", "briefcase", "robot", "envelope"], 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#262626"}, # Fond menu gris très foncé
        "icon": {"color": "#BCBCBC", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px", 
            "text-align": "center", 
            "margin":"0px", 
            "color": "#FFFFFF", # Texte blanc pour le contraste
            "--hover-color": "#444444"
        },
        "nav-link-selected": {"background-color": "#555555"}, # Case sélectionnée en gris moyen
    }
)

# 4. CONTENU DES SECTIONS
if selected == "Accueil":
    # Bannière (Image de montagne pour le look noir & blanc)
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80", use_column_width=True)
    st.markdown("""
        <div class="hero-text">
            <h1 style="color: white !important; text-shadow: 2px 2px 10px #000000; font-size: 60px;">- Noémie Victor -</h1>
            <p style="color: white !important; text-shadow: 2px 2px 10px #000000; font-size: 24px; font-style: italic;">Étudiante en Gestion des Ressources Humaines</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("##")
    st.write("### 🚀 À propos de moi")
    st.write("Alternante RH chez **NaTran** et étudiante à la **Sorbonne**, je m'oriente vers le métier de **Product Owner SIRH**.")

elif selected == "Compétences":
    st.header("🛠 Compétences & Outils")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 RH & Gestion")
        st.markdown("`Paie` `Intérim` `Onboarding` `Reporting`")
    with c2:
        st.subheader("💻 Digital & SIRH")
        st.markdown("`People Ask` `Streamlit` `Python` `Agilité`")
    
    st.divider()
    st.write("🌐 **Langues**")
    st.write("Français (Maternel)")
    st.progress(100)
    st.write("Anglais (B2)")
    st.progress(75)

elif selected == "Parcours":
    st.header("📊 Diplômes et Expériences")
    
    # Timeline style demandé (Noir & Blanc)
    etapes = [("2026-28", "Master SIRH (Cible)", "Sorbonne"),
              ("2025-26", "L3 Gestion RH", "Sorbonne"),
              ("2022-24", "DUT GEA", "UPEC")]
    
    for i, (annee, titre, ecole) in enumerate(etapes):
        col_a, col_b = st.columns([1, 4])
        with col_a: st.markdown(f"**{annee}**")
        with col_b:
            st.markdown(f"**{titre}**")
            st.caption(ecole)
            if i < len(etapes)-1: st.write("↑")

elif selected == "Contact":
    st.header("📬 Contact & Feedback")
    with st.form("contact"):
        st.text_input("Votre Email")
        st.text_area("Votre Feedback / Message")
        if st.form_submit_button("Envoyer"):
            st.success("Message reçu ! (Simulation)")
    
    st.write("---")
    st.write("🔗 **LinkedIn** : [Profil de Noémie](https://www.linkedin.com/)")
