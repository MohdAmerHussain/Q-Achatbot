Excel-based Q&A Chatbot
This project provides an Excel-based Q&A chatbot that leverages generative AI models to answer user queries about data stored in an Excel file. It uses FAISS for efficient similarity search and Google Generative AI for answering questions based on the retrieved data. The solution is built with Streamlit for the user interface, making it easy for users to upload an Excel file, ask questions, and get answers in real time.

Features
Excel File Upload: Upload an Excel file for analysis and generate a FAISS index.

Dynamic Query Handling: Ask questions related to the data, and receive answers generated based on the context from the Excel file.

Retrieval-Augmented Generation (RAG): Uses FAISS to search for relevant data, then feeds the retrieved data to a generative AI model for context-based answering.

Predefined FAQs: Offers predefined FAQs that users can click on to get answers.

Streamlit UI: A simple, interactive interface where users can upload files, input questions, and view responses.

Tech Stack
Streamlit: Framework for building interactive web apps.

FAISS: Facebook AI Similarity Search for efficient vector search.

LangChain: For text splitting, document management, and generating AI embeddings.

Google Generative AI: Used for retrieving context-based answers.

Pandas: For reading and processing Excel files.

OpenAI: (or equivalent model) used for generative answering based on context.

Prerequisites
To run this project locally, you need to have Python 3.x installed, along with the following dependencies:

streamlit

pandas

langchain

faiss-cpu or faiss-gpu

langchain-google-genai

openpyxl

os

styles (For custom CSS styling)

Install Dependencies
You can install all dependencies using the requirements.txt file:

bash
Copy
pip install -r requirements.txt
API Key for Google Generative AI
To interact with the Google Generative AI, you'll need to have a valid Google API Key. You can get the API key here.

Once you have the key, enter it in the Streamlit UI when prompted.

How to Use
Run the Application: Start the app by running the following command:

bash
Copy
streamlit run app.py
Upload Your Excel File:

Go to the sidebar in the Streamlit UI and upload an Excel file.

The file will be processed, and a FAISS index will be created.

Ask Questions:

After processing the Excel file, you can type your questions in the chat input field.

The chatbot will search for relevant data from the file and use the Google Generative AI model to generate an answer.

Predefined FAQs:

The sidebar also has predefined questions (e.g., "Describe the data?", "How many columns are numerical?", "What is the size of data?").

You can click these to quickly get answers without typing anything.

Code Structure
app.py: Main file containing the Streamlit UI and backend logic.

styles.py: Contains custom CSS for styling the Streamlit app.

requirements.txt: Lists the necessary dependencies for the project.

README.md: This file, providing project information.

Future Enhancements
Add support for multiple file formats (CSV, JSON, etc.).

Implement authentication for secure access to the chatbot.

Integrate more advanced document processing and filtering.

Add more interactive elements to the UI for better user experience.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Google Generative AI for the powerful language model.

FAISS for efficient vector-based similarity search.

Streamlit for providing an easy way to build and deploy interactive web apps.
