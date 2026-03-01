import streamlit as st
from streamlit_option_menu import option_menu

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Noémie VICTOR | Portfolio RH", layout="wide", page_icon="🚀")

# 2. STYLES PERSONNALISÉS (Texte noir, design épuré)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3, p, span, div { color: #1A1A1A !important; }
    
    /* Style du bouton de téléchargement bleu */
    .stDownloadButton button { 
        background-color: #004687 !important; 
        color: white !important; 
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
    }
    
    /* Positionnement du texte sur la bannière */
    .hero-text {
        text-align: center;
        margin-top: -280px; 
        padding-bottom: 180px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRE DE NAVIGATION HORIZONTALE
selected = option_menu(
    menu_title=None, 
    options=["À propos", "Compétences", "Parcours", "Chatbot IA"], 
    icons=["house", "tools", "briefcase", "robot"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "color": "#1A1A1A"},
        "nav-link-selected": {"background-color": "#004687", "color": "white"},
    }
)

# 4. CONTENU DES SECTIONS
if selected == "À propos":
    # Bannière style Nicolas Wadoux
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80", use_column_width=True)
    
    # Texte superposé avec ombre portée pour la lisibilité
    st.markdown("""
        <div class="hero-text">
            <h1 style="color: white !important; text-shadow: 3px 3px 10px #000000; font-size: 65px; font-weight: bold;">
                - Noémie Victor -
            </h1>
            <p style="color: white !important; text-shadow: 2px 2px 8px #000000; font-size: 26px; background: rgba(0,0,0,0.3); display: inline-block; padding: 10px 25px; border-radius: 15px;">
                Étudiante en Gestion des Ressources Humaines
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("##") # Espace
    
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("Photo Noemie.jpg", width=250)
        except:
            st.warning("📸 Photo Noemie.jpg non trouvée sur GitHub")
            
    with col2:
        st.write("### 📍 Présentation")
        st.write("""
        Actuellement en **Licence 3 RH à l'Université Paris 1 Panthéon-Sorbonne**, 
        j'évolue en tant qu'alternante chez **NaTran**. 
        
        Mon ambition est de devenir **Product Owner SIRH** afin d'allier la gestion humaine aux solutions technologiques innovantes.
        """)
        
        # Bouton CV sécurisé
        try:
            with open("CV.pdf", "rb") as file:
                st.download_button(
                    label="📥 Télécharger mon CV (PDF)", 
                    data=file, 
                    file_name="CV_Noemie_VICTOR.pdf", 
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.error("⚠️ Fichier 'CV.pdf' manquant sur GitHub.")

elif selected == "Compétences":
    st.header("🛠 Mes Compétences RH & Digitales")
    
    blocks = [
        ("📊 Expertise RH & Paie", ["Gestion des effectifs", "Cycle Intérim", "Onboarding", "EgaPro"]),
        ("💻 SIRH & Outils Digitaux", ["People Ask", "Saisie de flux RH", "Tableaux de bord", "Streamlit", "Python"]),
        ("⚙️ Gestion de Projet", ["Product Owner (Cible)", "Méthodologie Scrum", "SIRH Management"]),
        ("💡 Soft Skills", ["Adaptabilité", "Esprit d'analyse", "Travail en équipe", "Rigueur administrative"])
    ]
    
    c1, c2 = st.columns(2)
    for i, (title, skills) in enumerate(blocks):
        target = c1 if i % 2 == 0 else c2
        with target:
            st.subheader(title)
            st.markdown(" ".join([f"`{s}`" for s in skills]))

    st.divider()
    st.subheader("🌐 Langues")
    l1, l2 = st.columns(2)
    with l1:
        st.write("Français (Maternel)")
        st.progress(100)
    with l2:
        st.write("Anglais (Professionnel - B2)")
        st.progress(75)

elif selected == "Parcours":
    st.header("📊 Expériences & Formations")
    
    with st.expander("🏢 Alternance chez NaTran", expanded=True):
        st.write("""
        - **Pilotage RH :** Tenue de 6 tableaux de bord pour le suivi des effectifs.
        - **Gestion Administrative :** Cycle complet de l'intérim et rédaction pour les CSP.
        - **Outils :** Utilisation intensive du SIRH *People Ask*.
        """)
    
    st.divider()
    st.subheader("🎓 Éducation")
    st.write("- **2025-26 : Licence 3 GRH** | Université Paris 1 Panthéon-Sorbonne")
    st.write("- **2022-24 : DUT GEA** | IUT de Sénart-Fontainebleau (UPEC)")

elif selected == "Chatbot IA":
    st.header("🤖 Assistant IA Interactif")
    st.info("Posez-moi une question sur le parcours ou les compétences de Noémie !")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ex: Quelles sont ses missions chez NaTran ?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            p = prompt.lower()
            if any(word in p for word in ["mission", "natran", "fait"]):
                reponse = "Chez **NaTran**, Noémie pilote les effectifs et gère l'intérim via le SIRH People Ask."
            elif any(word in p for word in ["sorbonne", "école", "étude"]):
                reponse = "Elle est actuellement en L3 RH à la **Sorbonne**."
            else:
                reponse = "Je peux vous renseigner sur ses missions RH, ses compétences ou son parcours académique."
            
            st.markdown(reponse)
            st.session_state.messages.append({"role": "assistant", "content": reponse})
