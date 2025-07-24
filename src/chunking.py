# src/chunking.py
import re

def clean_text(txt):
    txt = re.sub(r"\s+", " ", txt)
    return txt.strip()

def chunk_text(txt, max_len=500):
    clean = clean_text(txt)
    words = clean.split()
    chunks, current = [], []
    curr_len = 0
    for w in words:
        current.append(w)
        curr_len += len(w)+1
        if curr_len >= max_len:
            chunks.append(" ".join(current))
            current, curr_len = [], 0
    if current:
        chunks.append(" ".join(current))
    return chunks

if __name__=="__main__":
    raw = open("data/raw_text.txt", encoding="utf-8").read()
    chunks = chunk_text(raw)
    for i, c in enumerate(chunks[:3]):
        print(i, c[:100])
