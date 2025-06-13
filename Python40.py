import streamlit as st

st.set_page_config(layout="wide")

# Left: Vimeo video
with st.container():
    st.markdown("### 🎥 Live Stream")
    vimeo_embed_url = "https://player.vimeo.com/video/1065266662?h=77b20e4768"
    st.components.v1.iframe(vimeo_embed_url, width=700, height=400)

# Right: Chat box
with st.container():
    st.markdown("### 💬 Chat")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Type your message here and press Enter")

    if user_input:
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Copilot", "Great thought, Poornima!"))

    for speaker, msg in st.session_state.chat_history:
        st.write(f"**{speaker}:** {msg}")