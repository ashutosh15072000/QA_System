from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import StorageContext,load_index_from_storage
from llama_index.core import ServiceContext
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model
from llama_index.core import VectorStoreIndex
import sys
from QAWithPDF.exception import customexception
from QAWithPDF.logger import logging

def download_gemini_embedding(model,document):
    """
    
    downloads and initialization a Gemini Embedding model for vector embeddings.

    returns:
    - vectorstoreIndex: An Index of vector emdedding for efficient similarity queries

    """

    try:
        logging.info("Creating Embedding.....")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        service_context = ServiceContext.from_defaults(llm=model,embed_model=gemini_embed_model, chunk_size=800, chunk_overlap=20)
        

        logging.info("Storing Vector Embeddings.....")
        index = VectorStoreIndex.from_documents(document,service_context=service_context)
        index.storage_context.persist()



        logging.info("Query Engine......")
        query_engine=index.as_query_engine()
        return query_engine
    except Exception as e:
        logging.info("Error Occured During Creating The Embeddings")
        raise customexception(e,sys)