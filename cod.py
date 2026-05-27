import streamlit as st

st.title("🌐 Empresas Parceiras")
col1, col2, col3 = st.columns(3)
with col1:
  st.image("mc-logo.png", use_container_width=True)
  st.title("MC Donald's ")
  st.link_button("Acessar","https://www.mcdonalds.com.br/")
  st.write("Maior empresa de fast food do mundo ")
with col2:
  st.image("netflix-logo.jpg", use_container_width=True)
  st.title("Netflix")
  st.link_button("Acessar","https://www.netflix.com/br/")
  st.write("Maior empresa de entretenimento do mundo")
with col3:
  st.image("nike-logo.png", use_container_width=True)
  st.title("Nike ")
  st.link_button("Acessar","http://nike.com.br/")
  st.write("Maior empresa de artigos esportivos do mundo ")
