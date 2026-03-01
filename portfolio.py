import streamlit as st
from streamlit_option_menu import option_menu

# 1. CONFIGURATION ET THÈME BLANC FORCÉ
st.set_page_config(page_title="Noémie VICTOR | Portfolio RH", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    h1, h2, h3, p, span, div, label { color: #1A1A1A !important; }
    .stDownloadButton button { background-color: #004687 !important; color: white !important; border-radius: 8px; }
    
    /* Style pour le texte sur la bannière d'accueil */
    .hero-text { text-align: center; margin-top: -250px; padding-bottom: 150px; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU DE NAVIGATION HORIZONTAL (Ajout de "Contact")
selected = option_menu(
    menu_title=None, 
    options=["Accueil", "Compétences", "Parcours", "Chatbot IA", "Contact"], 
    icons=["house", "tools", "briefcase", "robot", "envelope"], 
    orientation="horizontal",
    styles={
        "container": {"background-color": "#f8f9fa"},
        "nav-link-selected": {"background-color": "#004687"},
    }
)

# 3. CONTENU DES PAGES
if selected == "Accueil":
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80", use_column_width=True)
    st.markdown("""
        <div class="hero-text">
            <h1 style="color: white !important; text-shadow: 2px 2px 8px #000000; font-size: 60px;">Noémie VICTOR</h1>
            <p style="color: white !important; text-shadow: 2px 2px 8px #000000; font-size: 24px;">Étudiante en Gestion des Ressources Humaines</p>
        </div>
        """, unsafe_allow_html=True)
    st.write("### 🚀 Bienvenue sur mon Portfolio")
    st.write("Future Product Owner SIRH, actuellement en Licence 3 à la Sorbonne et alternante chez NaTran.")

elif selected == "Compétences":
    st.header("🛠 Mes Compétences")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 Expertise RH")
        st.markdown("`Gestion des effectifs` `Cycle Intérim` `Onboarding` `EgaPro`")
    with c2:
        st.subheader("💻 Digital & SIRH")
        st.markdown("`People Ask` `Tableaux de bord` `Streamlit` `Python`")

elif selected == "Parcours":
    st.header("📊 Mon Parcours Scolaire")
    
    # Timeline verticale comme demandé
    dates = [("2026-28", "Master SIRH (Objectif)", "Sorbonne"), 
             ("2025-26", "L3 Gestion RH", "Sorbonne"), 
             ("2022-24", "DUT GEA", "UPEC")]
    
    for i, (date, title, school) in enumerate(dates):
        col1, col2 = st.columns([1, 4])
        with col1: st.markdown(f"**{date}**")
        with col2:
            st.markdown(f"**{title}**")
            st.caption(school)
            if i < len(dates)-1: st.write("↑")
    
    st.divider()
    st.write("### 🏢 Expérience : Alternante RH @ NaTran")

elif selected == "Chatbot IA":
    st.header("🤖 Assistant Virtuel")
    st.info("Posez-moi une question sur le parcours de Noémie !")
    # ... (Ton code chatbot actuel peut être inséré ici)

elif selected == "Contact":
    st.header("📬 Me contacter / Laisser un Feedback")
    st.write("Un projet ? En plein recrutement ? N'hésitez pas à me laisser un message !")
    
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        # Formulaire de contact simulé
        with st.form("contact_form"):
            email = st.text_input("Votre adresse mail")
            objet = st.text_input("Objet")
            message = st.text_area("Votre message")
            submit = st.form_submit_button("Envoyer")
            
            if submit:
                if email and message:
                    st.success("Merci ! Votre message a bien été envoyé (simulation).")
                else:
                    st.error("Veuillez remplir les champs obligatoires.")
    
    with col_c2:
        st.write("### 🔗 Retrouvez-moi sur")
        st.link_button("LinkedIn : Noémie VICTOR", "https://www.linkedin.com/") # Remplace par ton lien
        st.write("---")
        try:
            with open("CV.pdf", "rb") as file:
                st.download_button("📥 Télécharger mon CV", data=file, file_name="CV_Noemie_VICTOR.pdf")
        except:
            st.error("CV non trouvé sur GitHub")
