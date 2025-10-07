import streamlit as st

st.title("🌟 My First Streamlit App")
st.write("Hello, this is my first Streamlit deployment!")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}!")
    from openAi import openAI
import streamlit as st
with st.sidebar:
   openAI_api_key = st.text_input("API Key", key="chatbot_api_key", type="password")


st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = openAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
