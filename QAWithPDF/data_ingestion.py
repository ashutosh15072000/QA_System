from llama_index.core import SimpleDirectoryReader
import sys
from QAWithPDF.exception import customexception
from QAWithPDF.logger import logging


def load_data(data):
    """
    Load PDF document from a specified directory.

    Parameters:
    - data(str): The path to the directory PDF file

    Returns:
    - Alist of loaded PDF documents.The specific type of documents may vary.
    
    """

    try:
        logging.info("Data Loading started.....")
        loader=SimpleDirectoryReader("Data")
        documents=loader.load_data()
        logging.info("Data Loading Completed...")
        return documents
    except Exception as e:
        logging.info("Error Occured During Loading Data....")
        raise customexception(e,sys)




