# Chunking Strategy Evaluation

## Fixed Chunking (healthcare_kb)

Precision@3:
- appointment booking = 1/1 = 1.0
- cancellation policy = 1/1 = 1.0
- follow up discount = 1/1 = 1.0
- telemedicine eligibility = 1/1 = 1.0
- insurance claim process = 1/1 = 1.0

Average Precision@3 = 1.0

Average Recall@3 = 1.0

---

## Sentence Chunking (healthcare_kb_sentence)

Precision@3:
- appointment booking = 1/1 = 1.0
- cancellation policy = 1/1 = 1.0
- follow up discount = 1/1 = 1.0
- telemedicine eligibility = 1/1 = 1.0
- insurance claim process = 1/1 = 1.0

Average Precision@3 = 1.0

Average Recall@3 = 1.0

---

## Recommendation

Both chunking strategies achieved Precision@3 = 1.0 and Recall@3 = 1.0 on the evaluation queries.

However, sentence-based chunking returned more focused and concise information, as shown by lower retrieval distances for several queries (e.g., telemedicine eligibility and insurance claim process).

Therefore, sentence-based chunking (`healthcare_kb_sentence`) was selected as the deployment collection for the LangGraph agent.

# Similarity Threshold Calibration

In-scope query distances ranged approximately from 0.52 to 1.22.

Out-of-scope query distances ranged approximately from 2.00 to 2.04.

Based on this observed separation, a threshold of 1.3 was selected.

Queries with distance greater than 1.3 trigger the fallback response:

"I don't know based on the available knowledge base."