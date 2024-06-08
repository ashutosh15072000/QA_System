import streamlit as st

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config("QA With Documents")

    doc=st.file_uploader("Upload Your Document")

    st.header("QA with Documents (Information Retrival)")

    user_question=st.text_input("Ask Your Queation?")

    if st.button("Submit"):
        with st.spinner("Processing..."):
            
            doc=load_data(doc)

            
            
            model=load_model()
            
            query_engine=download_gemini_embedding(model,doc)

            response =query_engine.query(user_question)

            st.write(response.response)


if __name__=="__main__":
    main()   