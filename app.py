import os
# [Fix] Force gRPC to use the system's native DNS resolver
os.environ["GRPC_DNS_RESOLVER"] = "native"


from QA_Rag.build_index import build_index
from QA_Rag.read_data import read_data
from QA_Rag.load_index import load_index
from QA_Rag.query_engine import query_engine

if __name__=="__main__":
    text_chunks=read_data("./data")
    embedding_index= build_index(text_chunks)
    query_engine(embedding_index, "What job role i am fit for?" )