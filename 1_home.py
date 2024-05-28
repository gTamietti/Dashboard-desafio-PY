import streamlit as st
import pandas as pd

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/games.csv",index_col=1, encoding='latin1')
    st.session_state["data"] = df_data

if "data_json" not in st.session_state:
    df_data_json =pd.read_json("datasets/games_metadata.json",lines=True) 
    st.session_state["data_json"] = df_data_json

st.header("Bem-vindo ao Nosso Site de Reviews de Jogos da Steam!")
st.divider()
st.markdown('Hello and welcome to our website dedicated to bringing you the best reviews and ratings of games available on the Steam platform. If you are a gaming enthusiast, you are in the right place!')
st.markdown("On Steam, you will find a vast collection of games from the most diverse genres, from exciting adventures to strategic challenges, captivating stories and electrifying multiplayer experiences. With so many options available, it can be difficult to decide which games are worth your attention and investment.")
st.markdown("That's where we come in! Our goal is to provide you with in-depth reviews, unbiased reviews, and honest opinions on the most popular games on Steam. We want to help you discover games that align with your interests, providing guaranteed moments of fun and entertainment.")
st.sidebar.markdown("Developed by Gabriel Tamietti Mauro")

