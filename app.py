from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model
from QAWithPDF.data_ingestion import load_data
from pathlib import Path
import os
import streamlit as st

import tempfile

def main():

        uploaded_file = st.file_uploader("File upload", type="pdf")
        user_question=st.text_input("Ask Your Queation?")
        if uploaded_file:
                temp_dir = tempfile.mkdtemp()
                path = os.path.join(temp_dir, uploaded_file.name)
                with open(path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                doc=load_data(temp_dir)
        
                if st.button("Submit"):
                        with st.spinner("Processing..."):
                                model=load_model()
                                query_engine=download_gemini_embedding(model,doc)
                                response =query_engine.query(user_question)
                                st.write(response.response)


  
if __name__=="__main__":
    main()  





