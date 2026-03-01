elif selected == "Parcours":
    st.header("📊 Mon Parcours Académique")
    st.write("Voici l'évolution de mon parcours étudiant vers mon projet de Master.")

    # --- SECTION TIMELINE ---
    st.write("### 📚 Mon Parcours Scolaire")
    st.write("") # ESPACE SIMPLE

    # ÉTAPE 1 : MASTER (HAUT) - Ton objectif futur
    c1, c2 = st.columns([1, 4])
    with c1: 
        st.markdown("**2026-28**")
    with c2: 
        st.markdown("**Master SIRH (Objectif)**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("↑") 

    # ÉTAPE 2 : L3 (MILIEU) - Ton année actuelle
    c3, c4 = st.columns([1, 4])
    with c3: 
        st.markdown("**2025-26**")
    with c4: 
        st.markdown("**Licence 3 Gestion, Parcours RH**")
        st.caption("Université Paris 1 Panthéon-Sorbonne")
        st.write("↑")

    # ÉTAPE 3 : DUT (BAS) - Ton diplôme obtenu
    c5, c6 = st.columns([1, 4])
    with c5: 
        st.markdown("**2022-24**")
    with c6: 
        st.markdown("**DUT Gestion des Entreprises et des Administrations**")
        st.caption("IUT de Sénart-Fontainebleau (UPEC)")

    st.divider()

    # --- SECTION EXPÉRIENCE ---
    st.write("### 🏢 Expérience chez NaTran")
    with st.expander("👉 Détails de mes missions d'alternance"):
        st.write("""
        - **Pilotage RH :** Tenue de 6 tableaux de bord pour le suivi des effectifs.
        - **Gestion Administrative :** Cycle complet de l'intérim et rédaction pour les CSP.
        - **Outils :** Utilisation intensive du SIRH *People Ask*.
        """)
