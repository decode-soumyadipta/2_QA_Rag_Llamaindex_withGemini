# Question-Answering System with RAG Architecture

This project implements a Retrieval-Augmented Generation (RAG) based question-answering system that leverages Google's Gemini language model and LlamaIndex for intelligent document querying. The system processes text documents, creates vector embeddings, and enables semantic search capabilities to answer queries based on the provided context.

## Overview

The application demonstrates a practical implementation of RAG architecture, where documents are first indexed using vector embeddings and then queried through a language model. This approach combines the strengths of information retrieval with the natural language understanding capabilities of large language models, resulting in contextually accurate and relevant responses.

## Technical Architecture

The system is organized into modular components that handle distinct aspects of the RAG pipeline:

- **Data Ingestion**: Reads and processes text documents from the data directory, preparing them for indexing
- **Index Building**: Converts documents into vector embeddings using Google's Gemini embedding model, creating a searchable vector store
- **Index Persistence**: Stores the generated index locally in the storage directory, allowing for efficient reuse without reprocessing
- **Query Engine**: Implements the retrieval and generation pipeline, fetching relevant document chunks and synthesizing answers using the Gemini LLM

The application utilizes LlamaIndex as the orchestration framework, which handles document chunking, embedding generation, vector storage, and query processing. The Gemini model serves dual purposes: generating embeddings for semantic search and producing natural language responses based on retrieved context.

## Key Features

- Vector-based semantic search for accurate information retrieval
- Persistent storage of indexes to minimize redundant processing
- Configurable LLM parameters for response generation
- Modular architecture enabling easy extension and maintenance
- Environment-based configuration for secure API key management

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

### Installation

1. Clone the repository and navigate to the project directory

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain a Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. Create a `.env` file in the root directory and add your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

### Running the Application

Execute the main application:
```bash
python app.py
```

The system will process the documents in the data directory, build the vector index, and answer the predefined query. You can modify the query in [app.py](app.py) to ask different questions based on your document content.
