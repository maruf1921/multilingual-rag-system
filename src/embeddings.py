
from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2")

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=True, convert_to_numpy=True).tolist()

if __name__=="__main__":
    from chunking import chunk_text
    raw = open("data/raw_text.txt", encoding="utf-8").read()
    chunks = chunk_text(raw)
    embeddings = embed_texts(chunks)
    with open("data/embeddings.json", "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks, "embeddings": embeddings}, f)
    print("Embeddings stored.")
