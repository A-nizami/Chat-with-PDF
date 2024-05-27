from langchain_community.chat_message_histories import StreamlitChatMessageHistory as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from Crypto.Cipher import AES
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


# Sidebar
with st.sidebar:
    st.title('Chat With PDF')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    -[Streamlit](https://streamlit.io/)
    -[LangChain](https://www.langchain.com/) 
    -[OpenAI](https://platform.openai.com/docs/models) LLM Model
    
                ''')
    add_vertical_space(5)
    st.write('Dev by [Niz]')


def main():
    st.header('Chat With PDF')
    
    load_dotenv()

    pdf = st.file_uploader("Upload Your PDF", type = 'pdf')
    #st.write(pdf)
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
             chunk_size=1000,
             chunk_overlap=200,
             length_function=len
            )
        chunks = text_splitter.split_text(text=text)
        #st.write(chunks)


        # embeddings
        embeddings = OpenAIEmbeddings()

        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        store_name = pdf.name[:-4]
        with open(f"{store_name}.pkl", "wb") as f:
             pickle.dump(VectorStore, f) 
             

if __name__=='__main__':
        main()