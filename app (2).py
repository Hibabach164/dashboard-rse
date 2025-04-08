
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données avec l'encodage correct
df = pd.read_csv("donnees_rse_1.csv", encoding="ISO-8859-1")

# Afficher les noms de colonnes pour le debug
st.write("Colonnes disponibles :", df.columns.tolist())

# Nettoyage des noms de colonnes s’il y a des espaces invisibles
df.columns = df.columns.str.strip()

st.title("Scores RSE")

# Sélecteurs
if "Entreprise" in df.columns and "Thème RSE" in df.columns:
    entreprises = df["Entreprise"].unique()
    themes = df["Thème RSE"].unique()

    selected_entreprise = st.selectbox("Choisir une entreprise", entreprises)
    selected_theme = st.selectbox("Choisir un thème RSE", themes)

    # Filtrage
    filtered_df = df[(df["Entreprise"] == selected_entreprise) & (df["Thème RSE"] == selected_theme)]

    # Affichage des indicateurs
    st.subheader("Indicateurs pour l'entreprise et le thème sélectionnés")
    st.dataframe(filtered_df)

    # Moyenne
    mean_score = filtered_df["Score"].mean()
    st.metric(label="Score moyen", value=f"{mean_score:.2f}")

    # Graphique
    st.subheader("Distribution des scores par thème")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df[df["Entreprise"] == selected_entreprise], x="Thème RSE", y="Score", estimator='mean', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.error("Les colonnes 'Entreprise' ou 'Thème RSE' sont manquantes.")
