# Research Paper Summarizer

A web-based tool that allows users to upload research papers in PDF format and receive concise, readable summaries using transformer-based models. Built using Streamlit, Hugging Face Transformers, and deployed on Render, this tool is designed to help students, researchers, and professionals quickly grasp the core content of lengthy academic documents.

---

## 🚀 Demo

**Live App:** [https://research-summarizer-flu9.onrender.com](https://research-summarizer-flu9.onrender.com)  
*(Free Render instance; may take ~30s to wake up)*

---

## ✨ Features

- Upload and parse research papers in **PDF** format.
- Cleanly extracts full text using `PyMuPDF`.
- Automatically splits long documents into **model-compatible chunks**.
- Summarizes using **DistilBART (`sshleifer/distilbart-cnn-12-6`)**, optimized for speed.
- Displays a clear, labeled summary of each section.
- Built with **Streamlit** for a fast, interactive user interface.
- Deployed on **Render** with support for public use.

---

## 🧠 How It Works

1. The PDF is parsed and converted to raw text.
2. Text is split into ~700-word chunks, respecting the token limits of the summarizer model.
3. Each chunk is passed through a transformer summarization model.
4. The final output is a merged list of clean, structured summaries.

---

## 🛠️ Tech Stack

| Component         | Technology                                |
|------------------|--------------------------------------------|
| Frontend         | [Streamlit](https://streamlit.io/)         |
| NLP Model        | `sshleifer/distilbart-cnn-12-6` (via 🤗)    |
| Text Extraction  | `PyMuPDF` (fitz)                           |
| Deployment       | [Render](https://render.com)               |
| Language         | Python                                     |



