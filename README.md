# Multilingual Retrieval-Augmented Generation (RAG) System

## Project Overview

This project implements a multilingual RAG system for answering English and Bengali queries using a Bengali PDF book (HSC26 Bangla 1st Paper). The system extracts text via OCR, chunks and embeds the content, retrieves relevant information, and generates answers using a local LLM (Ollama Mistral).

---

## Features

- Supports Bengali and English queries
- Retrieves relevant chunks from a pre-processed knowledge base
- Generates answers using the Ollama local LLM server
- Lightweight REST API for interaction
- OCR-based PDF-to-text extraction for Bengali scripts
- Semantic retrieval using cosine similarity

---

## Setup Guide

### Prerequisites

**Manual Installation Required:**  
- **Ollama** (LLM inference): [Download](https://ollama.com/download)
  - Verify: `ollama --version`
  - Run model: 
  ```
  ollama run mistral
  ```
- **Tesseract-OCR** (OCR for Bengali & English): [Download](https://github.com/tesseract-ocr/tesseract)
  - Add install path to your system’s Environment Variables (`Path`)
  - Add Bengali language:  
    - Select during install, or  
    - Download `ben.traineddata` from [tessdata](https://github.com/tesseract-ocr/tessdata) and copy to  
      `C:\Program Files\Tesseract-OCR\tessdata`

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd multilingual-rag
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **(Optional) Use a different PDF:**  
   Update the PDF filename in `src/preprocessing.py` (line 22):
   ```python
   pdf_file = os.path.join(base_dir, "data", "your_new_file.pdf")
   ```
   Then rerun steps 4 and 5 below.
   - If you're using the default hsc26_bangla1.pdf, you can skip steps 3–5.

4. **Convert PDF to raw text using OCR:**
   ```bash
   python src/ocr_preprocessing.py
   ```
5. **Generate text chunks and vector embeddings:**
   ```bash
   python src/embeddings.py
   ```
6. **Run the API server:**
   ```bash
   uvicorn src.api:app --reload
   ```

---

## API Usage ( Using postman )

- **Endpoint:**  
  `POST http://127.0.0.1:8000/ask`

- **Request body:**
  ```json
  {
    "query": "অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?"
  }
  ```

- **Response:** ( This may take a time )
  ```json
  {
    "answer": "শুম্ভুনাথ"
  }
  ```

---

## Tools & Libraries Used

- Sentence Transformers: `paraphrase-multilingual-mpnet-base-v2`
- pytesseract: OCR for Bengali PDF images
- pdf2image: Converts PDF pages to images for OCR
- FastAPI & uvicorn: REST API
- numpy: Vector operations and cosine similarity
- requests: HTTP requests to Ollama LLM API

---

## Sample Queries & Expected Outputs

| Query                                         | Expected Answer |
|-----------------------------------------------|----------------|
| অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?        | শুম্ভুনাথ      |
| কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে? | মামাকে         |
| বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?       | ১৫ বছর        |

---

## Evaluation Matrix

| Metric        | Description                                                | Approach                                 |
|---------------|-----------------------------------------------------------|------------------------------------------|
| Groundedness  | Answers are supported by retrieved context from knowledge base chunks. | Cosine similarity + retrieval check      |
| Relevance     | Retrieved chunks match the user query semantically and contextually. | Multilingual sentence embeddings         |

---

## Assessment Questions

- **Text extraction method:**  
  Used OCR-based extraction with pytesseract and pdf2image due to complex Bengali PDF formatting.
- **Chunking strategy:**  
  Cleaned text and split into ~500-character word-based chunks for balanced context.
- **Embedding model:**  
  Used `paraphrase-multilingual-mpnet-base-v2` for multilingual semantic embeddings.
- **Query and chunk comparison:**  
  Cosine similarity on normalized embedding vectors; embeddings stored in JSON.
- **Ensuring meaningful comparisons:**  
  Semantic embeddings and normalization help, but vague queries may need improved context or query expansion.
- **Improving relevance:**  
  Possible improvements: better OCR, dynamic chunk sizing, domain-specific embeddings, larger corpus.

- It performs well with English, but its support for Bangla is limited in the free version model.

---
