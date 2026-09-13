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
print(CHROMA_PATH)

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)
collection = client.get_collection(
    "healthcare_kb"
)
def retrieve_context(question):
    query_embedding = model.encode(
        question).tolist()
    results= collection.query(
        query_embeddings = [query_embedding], n_results = 5,
        include = ["documents","distances"]
    )
    documents = results["documents"][0]
    distance= results["distances"][0][0]
    print("Top Distance: ", distance)
    best_context = documents[0]
    return best_context, distance



    
question = (
    "Who won IPL  2024?"
)
context= retrieve_context(question)
print("\nQUESTION: ")
print(question)
print("\nRETRIEVED CONTEXT : ")
print(context)