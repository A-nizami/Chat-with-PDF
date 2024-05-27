# Chat With PDF

This app is an LLM-powered chatbot built using the following technologies:

- Streamlit
- LangChain
- OpenAI LLM Model

## About

The "Chat With PDF" app allows users to upload a PDF file, extract text from it, and interact with the content using LangChain's language model. It leverages Streamlit for the user interface and integrates LangChain's OpenAI embeddings for natural language understanding.

## How It Works

1. Users upload a PDF file.
2. The app extracts text from the PDF using the PyPDF2 library.
3. The text is split into smaller chunks using the RecursiveCharacterTextSplitter.
4. LangChain's OpenAI embeddings are used to create a vector store (FAISS) for efficient text retrieval.
5. Users can then chat with the PDF content using the chatbot interface.

## Development

- Developer: [Niz]
- Dev Environment: Set up your environment by loading the necessary environment variables.
- PDF Processing: Upload a PDF file, and the app will handle the rest.
- Vector Store: The app creates a vector store for efficient text retrieval.

Feel free to explore and enhance this app further! 🚀
