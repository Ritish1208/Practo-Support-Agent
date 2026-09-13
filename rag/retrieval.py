import os
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CHROMA_PATH = os.path.join(
    BASE_DIR,
    "chroma_db"
)

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)



collection = client.get_or_create_collection(name="healthcare_kb")
KB_PATH = "knowledge_base"
for filename in os.listdir(KB_PATH):
    file_path = os.path.join(
        KB_PATH,
        filename
    )
    with open(
        file_path,
        "r",
        encoding= "utf-8"
    ) as file:
        content = file.read()
        embedding = model.encode(
            content).tolist()
        collection.add (ids=[filename],
                         documents=[content],
                         embeddings=[embedding])

                                       
print(
    "Knowledge Base stored in ChromaDB!"
)    