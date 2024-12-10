import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize the app
st.set_page_config(page_title="LangGraph Query App", page_icon=":books:")
st.title("LangGraph Documentation Query App")

# Function to load and process data
@st.cache_resource
def load_data():
    # Load LangGraph documentation
    docs = WebBaseLoader("https://langchain-ai.github.io/langgraph/").load()
    
    # Split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200, chunk_overlap=100, add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)
    
    # Create embeddings and vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    texts = [doc.page_content for doc in all_splits]
    vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings)
    
    return vectorstore

# Load vectorstore
vectorstore = load_data()

# Set up retriever
retriever = vectorstore.as_retriever(search_type="similarity_score_threshold", search_kwargs={"k": 5, "score_threshold": 0.45})

groq_api_key = os.getenv("groq_api_key")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")
llm2 = ChatGroq(groq_api_key = groq_api_key, model_name = "llama-3.1-8b-instant")
# User input for question
question = st.text_input("Ask your question about LangGraph:")
    
if question:
        # Retrieve context and generate response
        retrieved_docs = retriever.invoke(question)
        context = ' '.join([doc.page_content for doc in retrieved_docs])
        
        if context:
            response = llm.invoke(f"""Answer the question according to the context given very briefly:
               Question: {question}.
               Context: {context}
            """)
            st.subheader("Response:")
            st.write(response.content)
        else:
            response = llm.invoke(f"""Answer the question according to the question very briefly and politely mention that the question asked is out of scope hence providing generic answer:
               Question: {question}.
               Context: {context}
            """)
            st.subheader("Response:")
            st.write(response.content)

# Footer
st.markdown("---")
st.markdown("**Created with LangChain and Groq API** :robot:")
