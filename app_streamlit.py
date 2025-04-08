
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données avec nettoyage
df = pd.read_csv("donnees_rse_1.csv", encoding="utf-8")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Titre
st.title("scores")

# Filtres
entreprises = df["entreprise"].unique()
themes = df["theme_rse"].unique()

selected_entreprise = st.selectbox("Choisir une entreprise", entreprises)
selected_theme = st.selectbox("Choisir un thème RSE", themes)

# Données filtrées
df_filtered = df[(df["entreprise"] == selected_entreprise) & (df["theme_rse"] == selected_theme)]

# Affichage score moyen
score_moyen = df_filtered["score_rse"].mean()
st.metric(label="Score RSE moyen", value=f"{score_moyen:.2f}")

# Histogramme des scores par indicateur
fig, ax = plt.subplots()
sns.barplot(data=df_filtered, x="indicateur", y="score_rse", ax=ax)
plt.xticks(rotation=45)
plt.title("Score RSE par indicateur")
st.pyplot(fig)
