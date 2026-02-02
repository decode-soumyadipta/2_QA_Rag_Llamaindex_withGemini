from llama_index.core import StorageContext, load_index_from_storage
import logging

def load_index(): 
    try:
        storage_context=StorageContext.from_defaults("./storage")
        return load_index_from_storage(storage_context)
    except Exception:
        logging.exception("Failed to load index from local storage")
        raise