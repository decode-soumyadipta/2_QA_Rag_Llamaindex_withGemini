from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.gemini import GeminiEmbedding
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

def build_index(documents):
    try:
        #Tell LlamaIndex which embedding model to use
        Settings.embed_model= GeminiEmbedding(
            model_name= "gemini-embedding-001",
            task_type= "retrieval_document",
            api_key= os.getenv("GOOGLE_API_KEY")
        )
        Settings.embed_batch_size = 1  # Process 1 chunk at a time
        Settings.chunk_size=800
        Settings.chunk_overlap=20
        
        #Build index (LlamaIndex handles embedding internally)
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        
        #persist index
        index.storage_context.persist(persist_dir="./storage")

        return index

    except Exception:
        logging.exception("Error in building index")
        raise






