import chromadb
from sentence_transformers import SentenceTransformer 
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
client = chromadb.PersistentClient( path= "chroma_db")
collection = client.get_collection("healthcare_kb")
query = ("Can I cancel my appointment?")
query_embedding = model.encode(query).tolist()
results = collection.query(
    query_embeddings = [query_embedding], n_results= 3
)
print("\nQUERY : ")
print(query)
print("\nTOP MATCHES")
for document in results["documents"][0]:
    print("\n------------------------")
    print(document)
