from sentence_transformers import SentenceTransformer
model = SentenceTransformer( "all-MiniLM-L6-v2")
sample_text = (
    "Patients may cancel appointments"
    "upto 24 hours before consultation."
)
embedding = model.encode(sample_text)
print("Embedding generated!")
print(f"Vector Length : {len(embedding)} ")
print(embedding[:10])