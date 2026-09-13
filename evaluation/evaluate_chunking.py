import os
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Get project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Point to the REAL ChromaDB
CHROMA_PATH = os.path.join(
    BASE_DIR,
    "rag",
    "chroma_db"
)

print("CHROMA PATH =", CHROMA_PATH)

# Connect to ChromaDB
client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

# Show available collections
print("\nAVAILABLE COLLECTIONS:")
for col in client.list_collections():
    print(col.name)

queries = [
    "appointment booking policy",
    "cancellation policy",
    "follow up discount",
    "telemedicine eligibility",
    "insurance claim process"
]

collections = [
    "healthcare_kb",
    "healthcare_kb_sentence"
]

for collection_name in collections:

    print("\n" + "=" * 50)
    print("COLLECTION:", collection_name)
    print("=" * 50)

    collection = client.get_collection(
        name=collection_name
    )

    for query in queries:

        query_embedding = model.encode(
            query
        ).tolist()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        print("\nQUERY:", query)

        if len(results["documents"][0]) > 0:

            print("\nTOP RESULT:")
            print(results["documents"][0][0][:500])

            print("\nDISTANCE:")
            print(results["distances"][0][0])

        else:
            print("No results found")