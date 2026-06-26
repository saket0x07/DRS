import os
import requests
import streamlit as st
from app.rag.chain import rag_chain

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="DOCUMENT RETRIEVAL ASSISTANT",
    page_icon="🤖",
    layout="wide"
)

# Apply custom styling to make the interface feel premium
st.markdown("""
<style>
    /* Main block paddings */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }
    
    /* Header sections styled nicely */
    .lhs-section-title {
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        color: #f1f5f9;
        margin-top: 1.25rem !important;
        margin-bottom: 0.75rem !important;
        border-bottom: 2px solid #334155;
        padding-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Document container for listing with custom scrollbar */
    .doc-scroll-list {
        max-height: 480px;
        overflow-y: auto;
        padding-right: 8px;
        border: 1px solid #1e293b;
        background-color: #0b0f19;
        border-radius: 8px;
        padding: 10px;
    }
    
    /* Custom scrollbar styling for Webkit */
    .doc-scroll-list::-webkit-scrollbar {
        width: 6px;
    }
    .doc-scroll-list::-webkit-scrollbar-track {
        background: #0f172a;
    }
    .doc-scroll-list::-webkit-scrollbar-thumb {
        background: #334155;
        border-radius: 4px;
    }
    .doc-scroll-list::-webkit-scrollbar-thumb:hover {
        background: #475569;
    }
    
    /* Document list item styling */
    .doc-card-item {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 8px 12px;
        margin-bottom: 6px;
        color: #cbd5e1;
        font-size: 0.85rem;
        font-family: 'Courier New', Courier, monospace;
        display: flex;
        align-items: center;
        gap: 6px;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
        transition: all 0.2s ease-in-out;
    }
    
    .doc-card-item:hover {
        background-color: #1e293b;
        border-color: #38bdf8;
        color: #ffffff;
        transform: translateX(2px);
    }
    
    /* Make buttons and fields blend in */
    .stButton>button {
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

def fetch_documents():
    try:
        response = requests.get(f"{API_URL}/documents", timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    
    # Fallback to local files if FastAPI backend is offline
    resume_dir = "app/data/resumes"
    if os.path.exists(resume_dir):
        return sorted([f for f in os.listdir(resume_dir) if f.endswith(".pdf")])
    return []

def upload_document(uploaded_file):
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
    try:
        response = requests.post(f"{API_URL}/upload", files=files, timeout=60)
        return response
    except Exception as e:
        return None

# Set up column layout: 30% LHS and 70% RHS
col_lhs, col_rhs = st.columns([0.3, 0.7])

with col_lhs:
    st.markdown('<div class="lhs-section-title"> Upload Document</div>', unsafe_allow_html=True)
    st.write("Upload a candidate resume PDF. Ingestion will run sequentially.")
    
    uploaded_file = st.file_uploader("Upload candidate profile", type=["pdf"], label_visibility="collapsed")
    if uploaded_file is not None:
        if st.button("Index Document", use_container_width=True, type="primary"):
            with st.spinner("Processing & ingesting document..."):
                response = upload_document(uploaded_file)
                if response and response.status_code == 200:
                    st.toast(f"Indexed {uploaded_file.name} successfully!", icon="✅")
                    st.success(f"Success: {uploaded_file.name} indexed.")
                    # Refresh page to update document library
                    st.rerun()
                else:
                    detail = response.json().get("detail", "Ingestion failed") if response else "Backend server offline."
                    st.error(f"Error: {detail}")

    st.markdown('<div class="lhs-section-title"> Document Library</div>', unsafe_allow_html=True)
    docs = fetch_documents()
    if docs:
        st.caption(f"Total: {len(docs)} documents indexed")
        # Render scrollable list
        doc_list_html = '<div class="doc-scroll-list">'
        for doc in docs:
            doc_list_html += f'<div class="doc-card-item">📄 {doc}</div>'
        doc_list_html += '</div>'
        st.markdown(doc_list_html, unsafe_allow_html=True)
    else:
        st.info("No documents indexed yet.")

with col_rhs:
    st.title(" DOCUMENT RETRIEVAL ASSISTANT")
    st.write("Interact with candidate files, search skills, compare resumes, or analyze profiles.")
    
    # Initialize chat state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Layout for clean history header
    col_hist_title, col_clear_btn = st.columns([0.8, 0.2])
    with col_clear_btn:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question about Documents..."):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate and display response
        with st.chat_message("assistant"):
            with st.spinner("Searching Documents and generating answer..."):
                try:
                    response = requests.post(f"{API_URL}/ask", json={"question": prompt}, timeout=60)
                    if response.status_code == 200:
                        answer = response.json()["answer"]
                    else:
                        answer = f"Error: Backend API returned {response.status_code}"
                except Exception:
                    # Fallback to local python invoke if FastAPI backend is not accessible
                    answer = rag_chain.invoke(prompt)
                
                st.write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})