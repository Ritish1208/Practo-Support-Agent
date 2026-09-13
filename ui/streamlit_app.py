import streamlit as st
import requests

# -------------------------------
# Session State
# -------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Practo Support Agent",
    page_icon="🏥",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:

    st.markdown("## 🏥 System Dashboard")

    st.success("🟢 FastAPI Connected")
    st.success("🟢 LangGraph Active")
    st.success("🟢 RAG Active")
    st.success("🟢 MCP Active")

    st.divider()

    with st.expander("📜 Query History"):

        if len(st.session_state.history) == 0:
            st.write("No queries yet.")

        for item in reversed(
            st.session_state.history
        ):

            st.markdown(
                f"**Q:** {item['query']}"
            )

            st.markdown(
                f"**A:** {item['response']}"
            )

            st.divider()

# -------------------------------
# Header
# -------------------------------
st.markdown("""
# 🏥 Practo Support Agent

### AI-Powered Healthcare Support System

Get instant answers to healthcare policies, appointment queries and patient support information.
""")



# User Query

query = st.text_input(
    "Ask a healthcare support question:"
)

if st.button("Submit"):

    if query:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={
                    "query": query
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.markdown("### 📋 Response")

                

                st.markdown(
    f"""
    <div style="
    padding:20px;
    border-radius:10px;
    background-color:#1E3A5F;
    color:white;
    border-left:5px solid #4CAF50;">
    {data["response"]}
    </div>
    """,
    unsafe_allow_html=True
)
                st.session_state.history.append(
                    {
                        "query": query,
                        "response": data["response"]
                    }
                )

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

        except Exception as e:

            st.error(
                f"Connection Error: {str(e)}"
            )


# Footer

st.markdown("---")

st.markdown(
    """
    <center>
    <h4>🏥 Practo Support Agent</h4>
    <p>Built using FastAPI, LangGraph, ChromaDB, MCP and Streamlit</p>
    <p>❤️ Built with love by Ritish Kumar</p>
    </center>
    """,
    unsafe_allow_html=True
)