import streamlit as st
from PIL import Image

#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="CustomAnything🤖")



#Title
st.markdown(
    """
    <h2 style='text-align: center;'>CustomAnything, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)


left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("https://media0.giphy.com/avatars/cabuu/uVaoNVXPobqj.gif")

st.markdown(
    """ 
    <h5 style='text-align:center;'><br><br><br>I'm CustomAnything, an intelligent chatbot. I use large language models to provide
    context-sensitive interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")

team_members_col1, team_members_col2 = st.columns(2)



hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



