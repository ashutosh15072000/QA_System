from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model
from QAWithPDF.data_ingestion import load_data
from pathlib import Path
data=Path('.\Data')
print(data)
doc=load_data(data)
print(doc)

# model=load_model()

# download_gemini_embedding(model,doc)


