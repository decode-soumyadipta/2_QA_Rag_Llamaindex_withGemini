from llama_index.core import SimpleDirectoryReader
import logging

logging.basicConfig(level=logging.INFO)


def read_data(data_path):
    try:
        logging.info('starting data loading...')
        loader= SimpleDirectoryReader(data_path)
        documents= loader.load_data()
        logging.info('loading data done...')
        return documents
    
    except Exception:
        logging.exception("Data loading failed")
        return None
        


#if __name__=="__main__":
#    load_data("../data")