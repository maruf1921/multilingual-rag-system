
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2")

def load_db(path="data/embeddings.json"):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    chunks = data["chunks"]
    embeddings = np.array(data["embeddings"])
    return chunks, embeddings

def retrieve(query, top_k=5):
    # Query encode
    q_emb = model.encode(query, convert_to_numpy=True, normalize_embeddings=True)

    # DB load
    chunks, emb = load_db()
    emb = emb / np.linalg.norm(emb, axis=1, keepdims=True)  # normalize

    # Cosine similarity
    sims = np.dot(emb, q_emb)

    # Top-k
    idx = np.argsort(-sims)[:top_k]

    return [(chunks[i], float(sims[i])) for i in idx]

if __name__ == "__main__":
    query = "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"
    results = retrieve(query)
    for i, (text, score) in enumerate(results):
        print(f"Rank {i+1} (Score: {score:.4f}):\n{text}\n")
