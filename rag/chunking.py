import os
import chromadb
from sentence_transformers import SentenceTransformer

KB_PATH = "knowledge_base"

documents = []

for filename in os.listdir(KB_PATH):
    file_path = os.path.join(KB_PATH, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    documents.append({
        "document_name": filename,
        "content": content
    })

print(f"Loaded {len(documents)} documents")

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="rag/chroma_db"
)

collection = client.get_or_create_collection(
    name="healthcare_kb"
)

client.delete_collection("healthcare_kb")

collection = client.get_or_create_collection(
    name="healthcare_kb"
)

for i, doc in enumerate(documents):
    embedding = model.encode(doc["content"]).tolist()

    collection.add(
        ids=[str(i)],
        documents=[doc["content"]],
        embeddings=[embedding],
        metadatas=[
            {"source": doc["document_name"]}
        ]
    )

print("Inserted:", collection.count())