import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage


st.set_page_config(layout="wide", page_title="Eletronics Recommender")


st.title("Eletronics Recommender")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in getattr(st.session_state, "messages"):
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("ai"):
            st.markdown(msg.content)

input_prompt = st.chat_input("Eletronic recommendation...")

if input_prompt:
    st.session_state["messages"].append(HumanMessage(content=input_prompt))

    with st.chat_message("user"):
        st.markdown(input_prompt)

    model = ""

    response = "Olá"

    st.session_state["messages"].append(AIMessage(content=response))

    with st.chat_message("ai"):
        st.markdown(response)
