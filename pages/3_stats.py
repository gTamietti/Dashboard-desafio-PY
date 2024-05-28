import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

#Recieve the CSV data
df_data = st.session_state["data"]

st.sidebar.markdown("Developed by Gabriel Tamietti Mauro")

#--------------Graphic1----------------------------->
jogos_mac = df_data['mac'].value_counts()

#subtitle descripton
label1 = ['Run on Mac', 'Doesen`t run on Mac']
#Access inside the 'mac' column the values of games who run on mac adn who doesn`t
value1 = [jogos_mac[True], jogos_mac[False]] 

#set the colors of each part of the pie graphic
graphic_colors1 = ["cornflowerblue", "darkorange"]

#labels = value of label1 ----  values = value of values1 ---- marker_colors = value of the colors defined in graphi_colors --- hole = put a hole inside the pie
fig1 = go.Figure(data=go.Pie(labels=label1, values=value1, marker_colors=graphic_colors1, hole=0.5))
fig1.update_layout(title_text="% of games that run on Mac", legend_title_text='Legenda:',
                   #dict is a python function used for created dictionarys, in this case is to organized the layout of the caption with the keys in the parentheses
                   legend=dict(orientation='h', xanchor='auto', x=0.5))
fig1.update_traces(textposition="inside", textinfo="percent")

#---------------Graphic2---------------------------->
jogos_win = df_data['win'].value_counts()

graphic_colors2 = ["limegreen", "mediumorchid"]

label2 = ['Run on Windows', 'Doesn`t run on Windows']
value2 = [jogos_win[True], jogos_win[False]] 

fig2 = go.Figure(data=go.Pie(labels=label2, values=value2, marker_colors=graphic_colors2, hole=0.5))
fig2.update_layout(title_text="% of games that run on Windows", legend_title_text='Legenda:',
                   legend=dict(orientation='h', xanchor='auto', x=0.5))
fig2.update_traces(textposition="outside", textinfo="percent")

#---------------Graphic3---------------------------->
jogos_lin = df_data['linux'].value_counts()

graphic_colors3 = ["crimson", "teal"]

label3 = ['Run on Linux', 'Doesen`t run on Linux']
value3 = [jogos_lin[True], jogos_lin[False]] 

fig3 = go.Figure(data=go.Pie(labels=label3, values=value3, marker_colors=graphic_colors3, hole=0.5))
fig3.update_layout(title_text="% of games that run on Linux", legend_title_text='Legenda:',
                   legend=dict(orientation='h', xanchor='auto', x=0.5))
fig3.update_traces(textposition="inside", textinfo="percent")

#-----------------Starting to show the data---------------->
col1, col2, col3 = st.columns(3)

#The update-layout is for customize the layout of fig[1,2,3]
#plotly_chart is a function of streamlit to show the graphics created by Plotly
#use_container_width is to agroup the itens of col[1,2,3] in a container
fig1.update_layout(title_font=dict(size=14))
col1.plotly_chart(fig1, use_container_width=True)

fig2.update_layout(title_font=dict(size=14))
col2.plotly_chart(fig2, use_container_width=True)

fig3.update_layout(title_font=dict(size=14))
col3.plotly_chart(fig3, use_container_width=True)

#------------------Bar Graphic------------------------------->
#I use value-counts because i wanna to access how many times each value of 'rating' column appear
#the reset_index is used to the values of rating and count recive an index and has a 2 columns DataFrame and keeping the original index
opcoes_rating = df_data['rating'].value_counts().reset_index() 
opcoes_rating.columns = ['rating', 'count']

#define the x and y and recives the data of opcoes_rating to show in a bar graphic with the px.bar
fig_rating = px.bar(opcoes_rating, x='rating', y='count', title='Avaliation counting')
st.plotly_chart(fig_rating)


