import streamlit as st
from pdf_parser import extract_text_from_pdf
from summarizer import summarize_text

st.set_page_config(page_title="Research Summarizer", page_icon=":book:", layout="wide")
st.title("Research Paper Summarizer")
st.write(
    "Upload your research paper in PDF format, and the app will summarize it for you.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text")
    st.text_area("Text from PDF", text[:3000] + "...", height=300)
    
    if text:
        st.subheader("Summary")
        if st.button("Summarize"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(text)
                st.success("Summary generated successfully!")
                st.write(summary)    
        