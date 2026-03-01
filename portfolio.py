import streamlit as st
from streamlit_option_menu import option_menu

# 1. Configuration (Wide mode pour occuper tout l'écran comme sur la photo)
st.set_page_config(page_title="Noémie VICTOR | RH", layout="wide")

# 2. Styles personnalisés (Texte noir, fond blanc)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3, p { color: #1A1A1A !important; }
    /* Style pour le bouton de téléchargement en haut à droite */
    .stDownloadButton { display: flex; justify-content: flex-end; margin-bottom: -50px; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRE DE NAVIGATION HORIZONTALE (L'icone en haut)
# On crée le menu avec des icônes pour chaque thème
selected = option_menu(
    menu_title=None, 
    options=["À propos", "Compétences", "Parcours", "Chatbot IA"], 
    icons=["house", "tools", "briefcase", "robot"], # Icônes automatiques
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#004687"},
    }
)

# 4. AFFICHAGE DES SECTIONS
if selected == "À propos":
    st.title("Noémie VICTOR")
    st.subheader("Future Product Owner SIRH")
    # Ajoute ton image de fond ou ta photo ici
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1350&q=80")
    st.write("Bienvenue sur mon espace professionnel.")

elif selected == "Compétences":
    st.header("🛠 Mes Compétences")
    # On remet ici tes blocs de compétences et tes barres de progression
    col1, col2 = st.columns(2)
    with col1:
        st.write("🇫🇷 Français")
        st.progress(100)
    with col2:
        st.write("🇬🇧 Anglais")
        st.progress(75)

elif selected == "Parcours":
    st.header("📊 Mon Expérience chez NaTran")
    st.write("Gestion des effectifs, intérim et SIRH.")

elif selected == "Chatbot IA":
    st.header("🤖 Mon Assistant Interactif")
    # On remet ici ton code de chatbot existant
