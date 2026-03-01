import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Noémie | Portfolio RH & SIRH", page_icon="🚀", layout="centered")

# 2. Design et Styles (FOND BLANC & TEXTE NOIR FORCÉ)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3, p, span, div, label, .stMarkdown { color: #1A1A1A !important; }
    .stChatMessage { border-radius: 15px; border: 1px solid #EEEEEE; background-color: #F8F9FA !important; }
    .stChatMessage p { color: #1A1A1A !important; }
    .stDownloadButton button { background-color: #004687 !important; color: white !important; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

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

# 3. MENU LATÉRAL (Navigation par thèmes)
with st.sidebar:
    st.title("📂 Menu")
    choix = st.radio(
        "Aller vers :",
        ["🏠 Qui suis-je ?", "🛠 Mes Compétences", "📊 Mon Parcours", "🤖 Chatbot Interactif"]
    )
    st.divider()
    # Le bouton de téléchargement est toujours accessible ici
    try:
        with open("CV.pdf", "rb") as file:
            st.download_button(
                label="📥 Télécharger mon CV",
                data=file,
                file_name="CV_Noemie_VICTOR.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("CV.pdf non trouvé")

# --- 4. AFFICHAGE DES SECTIONS SELON LE CHOIX DU MENU ---

if choix == "🏠 Qui suis-je ?":
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("Photo Noemie.jpg", width=200)
        except:
            st.warning("📸 Photo non trouvée")
    with col2:
        st.title("Noémie Charlène VICTOR")
        st.subheader("Future Product Owner SIRH")
        st.markdown("📍 **Alternante RH @NaTran**")
        st.markdown("🎓 **L3 RH @Paris 1 Panthéon-Sorbonne**")
    st.write("Passionnée par l'innovation digitale RH, je lie gestion humaine et outils technologiques.")

elif choix == "🛠 Mes Compétences":
    st.header("🛠 Mes Compétences RH & Digitales")
    blocks = [
        ("📊 Expertise RH & Paie", ["Gestion des effectifs", "Cycle Intérim", "Onboarding", "EgaPro"]),
        ("💻 SIRH & Outils Digitaux", ["People Ask", "Saisie de flux RH", "Tableaux de bord", "Streamlit", "Python"]),
        ("⚙️ Gestion de Projet & Agilité", ["Product Owner (Cible)", "Méthodologie Scrum", "SIRH Management"]),
        ("💡 Soft Skills", ["Adaptabilité", "Esprit d'analyse", "Travail en équipe", "Rigueur"])
    ]
    c1, c2 = st.columns(2)
    for i, (title, skills) in enumerate(blocks):
        target = c1 if i % 2 == 0 else c2
        with target:
            st.subheader(title)
            st.markdown(" ".join([f"`{s}`" for s in skills]))
    
    st.divider()
    st.subheader("🌐 Langues")
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.write("Français")
        st.progress(100)
    with col_l2:
        st.write("Anglais (B2)")
        st.progress(75)

elif choix == "📊 Mon Parcours":
    st.header("🏢 Expérience chez NaTran")
    with st.expander("👉 Détails de mes missions d'alternance"):
        st.write(CONNAISSANCES["missions"])
    
    st.divider()
    st.header("📚 Parcours Scolaire")
    st.markdown("**2025-26 : L3 Gestion RH** - Paris 1 Panthéon-Sorbonne")
    st.markdown("**2022-24 : DUT GEA** - UPEC")

elif choix == "🤖 Chatbot Interactif":
    st.header("🤖 Chatbot IA")
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
            if any(word in p for word in ["mission", "natran", "intérim"]):
                reponse = "Chez **NaTran**, je gère l'administratif et l'intérim via le SIRH."
            elif any(word in p for word in ["sorbonne", "étude", "master"]):
                reponse = "Je suis à la **Sorbonne** en L3 RH, visant un Master SIRH."
            else:
                reponse = "Je peux vous parler de mes missions, de mon école ou de mes compétences."
            st.markdown(reponse)
            st.session_state.messages.append({"role": "assistant", "content": reponse})
