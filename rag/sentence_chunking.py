import os
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="rag/chroma_db"
)

collection = client.get_or_create_collection(
    name="healthcare_kb_sentence"
)

KB_PATH = "knowledge_base"

for filename in os.listdir(KB_PATH):

    file_path = os.path.join(
        KB_PATH,
        filename
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    sentences = content.split(".")

    for i, sentence in enumerate(sentences):

        sentence = sentence.strip()

        if len(sentence) == 0:
            continue

        embedding = model.encode(
            sentence
        ).tolist()

        collection.add(
            ids=[f"{filename}_{i}"],
            documents=[sentence],
            embeddings=[embedding]
        )

print("Sentence chunks stored!")
print(
    "Total chunks:",
    collection.count()
)