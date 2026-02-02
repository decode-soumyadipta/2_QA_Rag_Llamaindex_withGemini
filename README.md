# QA System with RAG

A question-answering system built with RAG (Retrieval-Augmented Generation) using LlamaIndex and Google's Gemini model. Feed it your documents and ask questions—it finds relevant information and generates accurate answers.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/17d7df0c-013d-48fa-8872-bfae046b6177" />

## How It Works

The system follows a simple pipeline:

1. **Read Documents** - Loads text files from the `data/` folder
2. **Build Vector Index** - Converts documents into embeddings using Gemini's embedding model
3. **Store Locally** - Saves the index in `storage/` for reuse
4. **Query** - Retrieves relevant chunks and uses Gemini LLM to generate answers

Built with LlamaIndex for document processing and vector storage. Uses Gemini for both embeddings and response generation.

## Technical Stack

- **LlamaIndex** - Handles document chunking, indexing, and retrieval
- **Google Gemini** - Embedding model + LLM for answer generation
- **Vector Storage** - Persistent local storage for fast querying
- **Temperature: 0.15** - Low temperature for consistent, factual responses

## My Input & output (Tested)

<img width="756" height="501" alt="image" src="https://github.com/user-attachments/assets/1f8b4b79-2cf1-4c18-a363-3a030e52251a" />


## Setup & Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

3. Create `.env` file:
```
GOOGLE_API_KEY=your_api_key_here
```

4. Run the app:
```bash
python app.py
```

That's it. The system will index your documents and answer the query defined in [app.py](app.py). Change the query to ask different questions.
