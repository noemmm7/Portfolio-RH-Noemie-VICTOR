import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Noémie | Portfolio RH & SIRH", page_icon="🚀", layout="centered")

# 2. Design et Styles (FOND BLANC & TEXTE NOIR FORCÉ)
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* Force le texte en noir partout */
    h1, h2, h3, p, span, div, label, .stMarkdown {
        color: #1A1A1A !important;
    }

    /* Style des bulles de chat */
    .stChatMessage {
        border-radius: 15px; 
        border: 1px solid #EEEEEE;
        background-color: #F8F9FA !important;
    }
    
    .stChatMessage p {
        color: #1A1A1A !important;
    }

    /* Style des onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }

    /* Bouton de téléchargement bleu pro */
    .stDownloadButton button {
        background-color: #004687 !important;
        color: white !important;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. En-tête (Photo + Titre)
col1, col2 = st.columns([1, 2])
with col1:
    try:
        st.image("Photo Noemie.jpg", width=200)
    except:
        st.warning("📸 Photo Noemie.jpg non trouvée")

with col2:
    st.title("Noémie Charlène VICTOR")
    st.subheader("Future Product Owner SIRH")
    st.markdown("📍 **Alternante RH @NaTran**")
    st.markdown("🎓 **L3 RH @Paris 1 Panthéon-Sorbonne**")

st.divider()

# --- BASE DE CONNAISSANCES ---
CONNAISSANCES = {
    "missions": """
        - Transmission des courriers salariés et rédaction pour les **CSP**.
        - Pilotage de **6 tableaux de suivi** (Effectifs DAI, aides).
        - Gestion complète du cycle **intérim**.
        - Mise à jour des organigrammes et supports de communication RH.
    """,
    "agile": "Certifiée **Scrum Fundamental** et préparation de la **PSPO I**.",
    "qualites": "Autonomie, curiosité, adaptabilité et esprit d'équipe."
}

import streamlit as st

# --- SECTION COMPÉTENCES ---
st.header("🛠 Mes Compétences RH & Digitales")

# Organisation de tes compétences en colonnes pour un rendu "Tableau de Bord"
blocks = [
    ("📊 Expertise RH & Paie", ["Gestion des effectifs", "Cycle Intérim", "Onboarding", "Suivi des astreintes", "EgaPro"]),
    ("💻 SIRH & Outils Digitaux", ["People Ask", "Saisie de flux RH", "Tableaux de bord", "Streamlit", "Python (Notions)"]),
    ("⚙️ Gestion de Projet & Agilité", ["Product Owner (Cible)", "Méthodologie Scrum", "Rédaction de process", "SIRH Management"]),
    ("💡 Soft Skills", ["Adaptabilité", "Esprit d'analyse", "Travail en équipe", "Rigueur administrative"])
]

col1, col2 = st.columns(2)

# Boucle pour afficher tes blocs proprement
for i, (title, skills) in enumerate(blocks):
    target = col1 if i % 2 == 0 else col2
    with target:
        st.subheader(title)
        # Affichage sous forme de "tags" pour faire pro
        skill_tags = ""
        for s in skills:
            skill_tags += f" `{s}` "
        st.markdown(skill_tags)

st.divider()

# --- SECTION LANGUES ---
col_lang1, col_lang2 = st.columns([1, 2])

with col_lang1:
    st.subheader("🌐 Langues")

with col_lang2:
    # Barre de progression pour le Français
    st.write("Français (Langue maternelle)")
    st.progress(100)
    
    # Barre de progression pour l'Anglais
    st.write("Anglais (Niveau professionnel - B2)")
    st.progress(75)

st.info("💡 Ces compétences sont mobilisées quotidiennement dans mes missions d'alternance chez NaTran.")

# 4. Organisation par Onglets
tab1, tab2 = st.tabs(["💬 Chatbot IA", "📑 Mon Parcours & CV"])

with tab2:
    st.write("### 📄 Mon Curriculum Vitae")
    st.write("") # ESPACE SIMPLE
    st.write("") # ESPACE SIMPLE
    try:
        with open("CV.pdf", "rb") as file:
            st.download_button(
                label="📥 Télécharger mon CV (PDF)",
                data=file,
                file_name="CV Noémie VICTOR.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("❌ Fichier 'CV Noémie VICTOR.pdf' introuvable.")

    st.divider()

    # --- SECTION TIMELINE ---
    st.write("### 📚 Mon Parcours Scolaire")
    st.write("") # ESPACE SIMPLE
    st.write("") # ESPACE SIMPLE

    # ÉTAPE 1 : MASTER (HAUT)
    c1, c2 = st.columns([1, 4])
    with c1: 
        st.markdown("**2026-28**")
    with c2: 
        st.markdown("**Master SIRH (Objectif)**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("") # ESPACE SIMPLE
        st.write("↑") 
        st.write("") # ESPACE SIMPLE

    # ÉTAPE 2 : L3 (MILIEU)
    c3, c4 = st.columns([1, 4])
    with c3: 
        st.markdown("**2025-26**")
    with c4: 
        st.markdown("**Licence 3 Gestion, Parcours RH**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("") # ESPACE SIMPLE
        st.write("↑")
        st.write("") # ESPACE SIMPLE

    # ÉTAPE 3 : DUT (BAS)
    c5, c6 = st.columns([1, 4])
    with c5: 
        st.markdown("**2022-24**")
    with c6: 
        st.markdown("**DUT Gestion des Entreprises et des Administrations**")
        st.caption("IUT de Sénart-Fontainbleaau (UPEC)")
    st.divider()

    st.write("### 🏢 Expérience chez NaTran")
    st.write("") # ESPACE SIMPLE
    st.write("") # ESPACE SIMPLE
    with st.expander("👉 Détails de mes missions"):
        st.write(CONNAISSANCES["missions"])

with tab1:
    # 5. Chatbot
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Posez-moi une question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            p = prompt.lower()
            if any(word in p for word in ["mission", "natran", "fait", "travail", "intérim", "csp"]):
                reponse = "Chez **NaTran**, je m'occupe de l'administratif, des CSP et de l'intérim. Regardez l'onglet Parcours pour les détails !"
            elif any(word in p for word in ["sorbonne", "école", "parcours", "étude", "master"]):
                reponse = "Je suis en L3 RH à la **Sorbonne** et je vise un Master SIRH."
            elif any(word in p for word in ["cv", "télécharger"]):
                reponse = "Mon CV est disponible dans l'onglet **'Mon Parcours & CV'** ! 📄"
            else:
                reponse = "Je peux vous parler de mes missions, de mon école ou de mon CV. Que souhaitez-vous savoir ?"

            st.markdown(reponse)
            st.session_state.messages.append({"role": "assistant", "content": reponse})
