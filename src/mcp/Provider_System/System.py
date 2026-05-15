import json
import numpy as np
from mcp.central.brain_api import user_embeddings

MEMORY_FILE = "mcp/Provider_System/memory.json"


def upload_memory_System():
        try:
            with open(MEMORY_FILE, 'r',) as arhcive_json:
                return json.load(arhcive_json)
        except FileNotFoundError:
            return []
def save_memory_System(text):
        embedding = user_embeddings(text)
        if embedding is None:
            print("Error: Failed to generate embedding.")
            return
        memory = upload_memory_System()
        memory.append({"text": text, "embedding": embedding})
        with open(MEMORY_FILE, 'w') as arhcive_json:
            json.dump(memory, arhcive_json, indent=2)

def similarity(v1, v2):
     v1, v2 = np.array(v1), np.array(v2)
     return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

def search_similarity_System(text, limit=0.75):
    embedding_input = user_embeddings(text)
    memory = upload_memory_System()

    if not memory or embedding_input is None:
        return None
    
    results = [
         (item['text'], similarity(embedding_input, item['embedding']))
         for item in memory
    ]

    closer_results = max(results, key=lambda x: x[1])
    if closer_results[1] >= limit:
        return closer_results[0]
    else:
        return None