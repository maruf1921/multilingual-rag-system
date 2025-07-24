import requests
import json
from src.retriever import retrieve 

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(query):
    docs = retrieve(query, top_k=3)
    context = "\n".join([d[0] for d in docs])

    prompt = f"{context}\n\nপ্রশ্ন: {query}\nউত্তর:"

    payload = {
        "model": "mistral",  # বা llama3 
        "prompt": prompt,
        "stream": False
    }

    print("=== DEBUG: Prompt Sent ===")
    print(prompt)
    print("==========================")

    response = requests.post(OLLAMA_URL, data=json.dumps(payload))
    response.raise_for_status()

    answer = response.json()["response"]

    print("=== DEBUG: Generated Answer ===")
    print(answer)
    print("================================")

    return answer

if __name__ == "__main__":
    sample_question = "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"
    print("Sample Question:", sample_question)
    print("Answer:", generate_answer(sample_question))
