import chromadb

paths = [
    "chroma_db",
    "rag/chroma_db",
    "rag/chromadb_db"
]

for path in paths:
    try:
        print("\nPATH:", path)

        client = chromadb.PersistentClient(path=path)

        for col in client.list_collections():
            collection = client.get_collection(col.name)
            print(
                col.name,
                "->",
                collection.count()
            )

    except Exception as e:
        print("ERROR:", e)