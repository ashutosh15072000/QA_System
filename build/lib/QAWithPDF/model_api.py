import os 
from dotenv import load_dotenv
import sys
from llama_index.llms.gemini import Gemini
from IPython.display import Markdown,display
import google.generativeai as genai
from QAWithPDF.exception import customexception
from QAWithPDF.logger import logging

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
     """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
     try:
          logging.info("Loading Model......")
          model=Gemini(model="models/gemini-pro")
          return model
     
     except Exception as e:
          logging.info("Error Occured During Model Loading.....")
          raise customexception(e,sys)