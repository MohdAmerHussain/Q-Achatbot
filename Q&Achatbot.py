# import streamlit as st
# import pandas as pd
# from langchain.schema import Document
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores.faiss import FAISS
# from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
# import os
# from styles import *

"""
This script implements an Excel-based Q&A chatbot using Streamlit and Google Generative AI.

The application allows users to upload an Excel file, process its data, and interact with the chatbot by asking questions related to the file.
Key libraries used in this script:
- Streamlit: Web framework for creating interactive apps.
- Pandas: Library for data manipulation and processing Excel files.
- LangChain: For document processing and integrating generative AI models.
- FAISS: For efficient similarity search over large datasets.
- Google Generative AI: For generating responses based on retrieved context.

The script handles:
- Uploading an Excel file and creating a FAISS index.
- Processing and splitting documents into smaller chunks for efficient search.
- Using a generative model to answer questions based on the context retrieved.

Dependencies:
- streamlit
- pandas
- langchain
- faiss-cpu or faiss-gpu
- langchain-google-genai
- openpyxl
"""

# Import necessary libraries for the application

import streamlit as st  # Streamlit: A framework to build interactive web applications quickly and easily.
import pandas as pd  # Pandas: A data manipulation and analysis library, useful for reading and processing Excel files.

# LangChain-related imports for document processing and AI integration
from langchain.schema import Document  # Document: Represents a text document in LangChain for processing.
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting text into smaller chunks based on characters.
from langchain.vectorstores.faiss import FAISS  # FAISS: A library for efficient similarity search, used for indexing and querying documents.

# Google Generative AI-related imports
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings  # Google Generative AI for generating text-based answers.

import os  # os: Provides functions for interacting with the operating system, such as setting environment variables.
from styles import *  # Custom styling for the Streamlit app (presumably a separate module with custom CSS or styling logic).


# Function to prepare the Excel file, split text, and create a FAISS index
def prepare_excel(file_path, nrows=10000, skip_rows=0):
    """
    Reads the Excel file, processes the data, and creates a FAISS index for fast similarity search.
    """
    # Read the Excel file with the specified number of rows and skip rows
    chunk = pd.read_excel(file_path, engine='openpyxl', header=0, skiprows=range(1, skip_rows + 1), nrows=nrows)
    
    # Check if the chunk is empty after reading the data
    if chunk.empty:
        print("No data to process in the specified range.")
        return None

    # Prepare data by converting each row into a string, retaining column names
    header_row = chunk.columns.tolist()  # Get column names
    data_with_header = pd.DataFrame([header_row], columns=chunk.columns)  # Add header as a row
    chunk_data = pd.concat([data_with_header, chunk], ignore_index=True)  # Combine header with the data
    chunk_data = chunk_data.astype(str).apply(lambda row: ' '.join(row), axis=1).tolist()  # Flatten into strings
    
    # Convert the processed data into Document objects for text processing
    documents = [Document(page_content=text) for text in chunk_data]

    # Split the documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    chunked_data = text_splitter.split_documents(documents)

    # Generate embeddings for each chunk using the provided model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    # Create a FAISS index from the documents
    db_fiass = FAISS.from_documents(chunked_data, embedding=embeddings)
    
    return db_fiass

# Function to perform retrieval-augmented generation (RAG)
def rag(db_fiass, Query, k=10):
    """
    Perform retrieval-augmented generation (RAG) by searching the FAISS index for the most relevant documents
    and using a generative model to generate an answer based on the retrieved context.
    """
    # Perform similarity search on the FAISS index
    output_retrieval = db_fiass.similarity_search(Query, k=k)
    
    # Merge the retrieved documents into a single context string
    output_retrieval_merged = "\n".join([doc.page_content for doc in output_retrieval])
    
    # Enhanced prompt formulation for the generative model
    Prompt = f"""
    You are a helpful assistant with access to the following context:

    {output_retrieval_merged}

    Your task is to answer the following question based on the provided context. 

    Question: {Query}

    Please provide your answer in a clear, concise, and structured format. If the information is available, break your answer into key points. 
    If the context does not contain enough information to answer the question, kindly respond by saying, "I don't have enough information to answer that."

    Be direct and accurate with your response. If the question asks for a list, summary, or specific data, format your answer accordingly.
    """
    
    # Instantiate the generative model
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0)
    
    # Generate the response using the model
    response_text = model.invoke(Prompt)
    return response_text.content

# Function to set up the chatbot UI and logic
def chatbot_logic():
    """
    Streamlit UI for the Excel-based Q&A chatbot, including file upload, API key input, and interaction with the user.
    """
    # Streamlit UI Configuration
    st.set_page_config(page_title="Excel-based Q&A Chatbot", page_icon="🤖", layout="wide")
    styles_css()  # Apply custom styles
    
    # Columns layout for header and Google API Key input
    c3, c4 = st.columns([2, 1])
    with c3:
        st.title("💬 Excel-based Q&A Chatbot")
    with c4:
        # Input for Google API Key
        google_api_key = st.text_input("Enter your Google API Key", type="password", help="https://ai.google.dev/gemini-api/docs/api-key")
    
    # Sidebar: File uploader and Google API Key input
    uploaded_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx"])

    # Session State Initialization
    if 'db_fiass' not in st.session_state:
        st.session_state.db_fiass = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Handle File Upload and Processing
    if uploaded_file:
        st.sidebar.success("File uploaded successfully!")
        
        # Option to specify skip_rows and chunk size for processing
        with st.sidebar.expander("Skip rows and chunk size:"):
            c1, c2 = st.columns(2)
            with c1:
                start_rows = st.number_input("Skip Rows", min_value=0, max_value=600000, value=0)
            with c2:
                nrows = st.number_input("Rows per chunk", min_value=1, max_value=700000, value=10000)
            submit_button = st.button(label="Process File")
        
        if submit_button:
            # Set the Google API Key
            if google_api_key:
                os.environ["GOOGLE_API_KEY"] = google_api_key
                st.sidebar.success("Google API key set successfully!")
            else:
                st.sidebar.error("Please enter a valid Google API key.")

            # Process the uploaded Excel file and create a FAISS index
            db_fiass = prepare_excel(uploaded_file, nrows=nrows, skip_rows=start_rows)
            if db_fiass:
                st.session_state.db_fiass = db_fiass
                st.sidebar.success("Excel file processed successfully!")
            else:
                st.sidebar.error("Error processing the Excel file. Please check the file format.")

    # Chat container to display messages
    prompt_placeholder = st.empty()
    with prompt_placeholder.container(height=450):
        if len(st.session_state.messages) > 0:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.write(message["message"])
                elif message["role"] == "assistant":
                    with st.chat_message("assistant"):
                        st.write(message["message"])

        # Function to process the user's chat input
    def process_chat_input(user_input):
        if user_input and st.session_state.db_fiass:
            # Generate the answer using RAG method
            answer = rag(st.session_state.db_fiass, user_input)
            
            # Append user input and assistant response to the chat history
            st.session_state.messages.append({"role": "user", "message": user_input})
            st.session_state.messages.append({"role": "assistant", "message": answer})

            # Display the assistant's response
            st.chat_message("assistant").markdown(answer)
        else:
            st.error("Please upload a file and process it before asking a question.")
    
    # Predefined FAQ questions with buttons in the sidebar
    faq_questions = ["Describe the data?", "How many columns are numerical?", "What is the size of data?"]
    for question in faq_questions:
        if st.sidebar.button(question):
            process_chat_input(question)
            st.rerun()

    # Manual input from the user
    if user_input := st.chat_input("Ask a question..."):
        process_chat_input(user_input)
        st.rerun()

# Run the chatbot logic
if __name__ == "__main__":
    chatbot_logic()
