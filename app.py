import streamlit as st
from src.rag_pipeline import ask

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Offline PDF RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Offline PDF RAG Chatbot")
st.caption("Answers are generated ONLY from the uploaded document.")

# -------------------------------
# Session State Initialization
# -------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# User Input
# -------------------------------
with st.form("chat_form", clear_on_submit=True):
    question = st.text_input(
        "Ask a question about the document",
        placeholder="e.g. What benefits did executives receive this year?"
    )
    show_context = st.checkbox("Show retrieved context (debug mode)")
    submit = st.form_submit_button("Ask")

# -------------------------------
# Handle Question
# -------------------------------
if submit and question.strip():
    if show_context:
        answer, contexts = ask(question, show_context=True)
    else:
        answer = ask(question)
        contexts = []

    st.session_state.chat_history.append({
        "question": question,
        "answer": answer,
        "contexts": contexts
    })

# -------------------------------
# Display Chat History
# -------------------------------
for chat in reversed(st.session_state.chat_history):
    st.markdown("### 🧑 You")
    st.write(chat["question"])

    st.markdown("### 🤖 Bot")
    st.write(chat["answer"])

    if show_context and chat["contexts"]:
        with st.expander("🔍 Retrieved document chunks"):
            for i, chunk in enumerate(chat["contexts"], 1):
                st.markdown(f"**Chunk {i}:**")
                st.write(chunk)

    st.divider()
