from llama_index.llms.gemini import Gemini
from llama_index.core import Settings
from dotenv import load_dotenv
import logging
import os

from QA_Rag.load_index import load_index

load_dotenv()


def query_engine(index, query):
    try:
        Settings.llm= Gemini(
        model="gemini-3-flash-preview",
        api_key= os.getenv("GOOGLE_API_KEY"),
        temperature=0.15,
        )
        
        query_engine = index.as_query_engine()
        response = query_engine.query(query)
        print(response)

    except Exception:
        logging.exception("LLM Failed")
        raise

