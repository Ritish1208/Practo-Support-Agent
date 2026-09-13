# check_count.py

import chromadb
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CHROMA_PATH = os.path.join(
    BASE_DIR,
    "rag",
    "chroma_db"
)

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

for col in client.list_collections():

    collection = client.get_collection(
        col.name
    )

    print(
        col.name,
        "->",
        collection.count()
    )