
import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Tableau de bord RSE - Analyse des scores")

# Chargement des données avec encodage correct
df = pd.read_csv("donnees_rse_1.csv", encoding='latin-1')

# Filtres
entreprises = df["Entreprise"].unique()
themes = df["Thème RSE"].unique()

selected_entreprise = st.selectbox("Choisir une entreprise", ["Toutes"] + list(entreprises))
selected_theme = st.selectbox("Choisir un thème RSE", ["Tous"] + list(themes))

# Filtrage
filtered_df = df.copy()
if selected_entreprise != "Toutes":
    filtered_df = filtered_df[filtered_df["Entreprise"] == selected_entreprise]
if selected_theme != "Tous":
    filtered_df = filtered_df[filtered_df["Thème RSE"] == selected_theme]

# Affichage des données filtrées
st.subheader("Données filtrées")
st.dataframe(filtered_df)

# Statistiques
if not filtered_df.empty:
    st.subheader("Statistiques")
    st.metric("Score moyen", round(filtered_df["Score RSE"].mean(), 2))
    st.metric("Score maximum", round(filtered_df["Score RSE"].max(), 2))
    st.metric("Score minimum", round(filtered_df["Score RSE"].min(), 2))
else:
    st.warning("Aucune donnée disponible avec les filtres sélectionnés.")
