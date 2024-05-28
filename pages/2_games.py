import streamlit as st
import pandas as pd

df_data = st.session_state["data"]
df_data_json=st.session_state["data_json"]

if "level_0" in df_data.columns:
    df_data.drop("level_0", axis=1, inplace=True)
df_data.reset_index(inplace=True)

jogos = df_data['title'].value_counts().index
jogo = st.sidebar.selectbox('Jogos', jogos)

st.sidebar.markdown("Developed by Gabriel Tamietti Mauro")

game_stats = df_data[df_data["title"] == jogo].iloc[0]

descricao = df_data_json[df_data_json["app_id"] == game_stats["app_id"]]["description"].values[0]

st.title(game_stats['title'])

col1, col2, col3 = st.columns(3)

col1.markdown(f"**User Reviews:** {game_stats['user_reviews']}")
col2.markdown(f"**Price:** ${game_stats['price_final']}")
col3.markdown(f"**Date release:** {game_stats['date_release']}")

st.write("Game description:")
st.write(descricao)

st.divider()
st.subheader(f"Rating: {game_stats['rating']}")
st.subheader(f"Overall: {game_stats['positive_ratio']}")
st.progress(int(game_stats['positive_ratio']))



