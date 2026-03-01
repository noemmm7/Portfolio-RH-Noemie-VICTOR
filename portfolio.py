import streamlit as st
from streamlit_option_menu import option_menu

# 1. CONFIGURATION (TOUJOURS EN PREMIER ET TOUT À GAUCHE)
st.set_page_config(page_title="Noémie VICTOR | Portfolio", layout="wide")

# 2. DESIGN GRIS & NOIR
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    h1, h2, h3, p, span, div, label { color: #1A1A1A !important; }
    .stDownloadButton button { background-color: #333333 !important; color: white !important; border-radius: 4px; }
    .hero-text { text-align: center; margin-top: -260px; padding-bottom: 160px; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRE DE NAVIGATION
selected = option_menu(
    menu_title=None, 
    options=["Accueil", "Compétences", "Parcours", "Chatbot IA", "Contact"], 
    icons=["house", "tools", "briefcase", "robot", "envelope"], 
    orientation="horizontal",
    styles={
        "container": {"background-color": "#262626"},
        "nav-link": {"color": "#FFFFFF"},
        "nav-link-selected": {"background-color": "#555555"},
    }
)

# 4. CONTENU DES SECTIONS
if selected == "Accueil":
    # Bannière
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80", use_column_width=True)
    st.markdown("""
        <div class="hero-text">
            <h1 style="color: white !important; text-shadow: 2px 2px 10px #000000; font-size: 60px;">- Noémie Victor -</h1>
            <p style="color: white !important; text-shadow: 2px 2px 10px #000000; font-size: 24px;">Étudiante en Gestion des Ressources Humaines</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("##")
    
    # PHOTO À CÔTÉ DU TEXTE
    col_photo, col_texte = st.columns([1, 2])
    with col_photo:
        try:
            st.image("Photo Noemie.jpg", width=300)
        except:
            st.warning("📸 Photo Noemie.jpg non trouvée sur GitHub")
            
    with col_texte:
        st.write("### 📍 À propos de moi")
        st.write("""
        Actuellement en **Licence 3 RH** à l'Université Paris 1 Panthéon-Sorbonne, 
        je développe mes compétences en alternance chez **NaTran**. 
        
        Passionnée par l'innovation digitale appliquée aux RH, je m'oriente vers le métier 
        de **Cheffe de Projets SIRH**.
        """)

elif selected == "Compétences":
    st.header("🛠 Mes Compétences")
    st.write("Gestion des effectifs, SIRH People Ask, Agilité.")

elif selected == "Parcours":
    st.header("📊 Mon Parcours Académique")
    # Ta timeline ici...

elif selected == "Contact":
    st.header("📬 Contact")
    st.write("Laissez-moi un message !")
