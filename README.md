# LangGraph Documentation Query App
[LINK TO APP](https://chatwithlanggraphdocumentation.streamlit.app/)


## Overview

The LangGraph Documentation Query App is a sophisticated question-answering bot designed to provide accurate and concise responses to queries based on LangGraph's official documentation. Leveraging Retrieval-Augmented Generation (RAG) architecture, the app offers seamless and intelligent access to LangGraph documentation.

## 🌟 Features

- **Precise Documentation Queries**: Accurately answers questions related to LangGraph
- **Smart Query Handling**: Gracefully manages out-of-scope questions
- **Advanced Retrieval**: Utilizes FAISS for efficient document retrieval
- **Semantic Understanding**: Powered by HuggingFace embeddings
- **Flexible LLM Integration**: Supports multiple Groq LLM models

## 🏗️ Architecture

The app follows a comprehensive pipeline:

1. **Data Scraping**: Extracts documentation from LangGraph
2. **Text Processing**: Splits content into manageable chunks
3. **Embedding Generation**: Creates semantic embeddings using `all-MiniLM-L6-v2`
4. **Vector Storage**: Employs FAISS for fast, efficient retrieval
5. **Response Generation**: Uses Groq LLM models to craft precise answers

## 🚀 Installation

### Prerequisites

- Python 3.9+
- Groq API Key

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   cd your-repo-url
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment:
   - Create a `.env` file
   - Add your Groq API key:
     ```
     groq_api_key=YOUR_GROQ_API_KEY
     ```

4. Launch the app:
   ```bash
   streamlit run app.py
   ```

## 📋 Requirements

- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq API

## 🛠️ Technologies

- **Language Processing**: LangChain
- **Vector Database**: FAISS
- **Embeddings**: HuggingFace
- **LLM**: Groq (Gemma2-9b-It, llama-3.1-8b-instant)

## 📝 Usage

1. Open the application
2. Enter your LangGraph-related query
3. Receive accurate, context-aware response


**Created by:** Sarthak Pandey
