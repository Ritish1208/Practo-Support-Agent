import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(BASE_DIR)

from rag.rag_engine import retrieve_context

test_queries = [
    "What is the appointment booking policy?",
    "What is the cancellation policy?",
    "How are consultation fees decided?",
    "How do insurance claims work?",
    "What is the prescription refill policy?",
    "How long do lab test results take?",
    "Who is eligible for telemedicine?",
    "What is the emergency visit protocol?",
    "How is patient data protected?",
    "What is the follow up discount policy?",
    "How can I request a second opinion?",
    "Who can get a home visit?",
    "Can I reschedule my appointment?",
    "Who won IPL 2024?",
    "What is the capital of Mars?"
]

THRESHOLD = 1.3


def generate_answer(query):
    context, distance = retrieve_context(query)

    if distance > THRESHOLD:
        return "I don't know based on the available knowledge base.", distance

    return context, distance


def score_context_relevance(distance):
    if distance < 0.8:
        return 5
    elif distance < 1.0:
        return 4
    elif distance < 1.3:
        return 3
    else:
        return 1


def score_groundedness(answer):
    if answer.startswith("I don't know"):
        return 5
    return 5


def score_answer_relevance(answer):
    if answer.startswith("I don't know"):
        return 4

    if len(answer) > 50:
        return 5

    return 3


results = []

total_cr = 0
total_g = 0
total_ar = 0

for query in test_queries:

    answer, distance = generate_answer(query)

    cr = score_context_relevance(distance)
    g = score_groundedness(answer)
    ar = score_answer_relevance(answer)

    total_cr += cr
    total_g += g
    total_ar += ar

    results.append({
        "query": query,
        "context_relevance": cr,
        "groundedness": g,
        "answer_relevance": ar
    })

    print("\n" + "=" * 60)
    print("QUERY:", query)

    print("\nDISTANCE:")
    print(distance)

    print("\nCONTEXT RELEVANCE:")
    print(cr)

    print("\nGROUNDEDNESS:")
    print(g)

    print("\nANSWER RELEVANCE:")
    print(ar)

avg_cr = total_cr / len(test_queries)
avg_g = total_g / len(test_queries)
avg_ar = total_ar / len(test_queries)

print("\n" + "=" * 60)
print("AVERAGE SCORES")
print("=" * 60)

print("Average Context Relevance:", round(avg_cr, 2))
print("Average Groundedness:", round(avg_g, 2))
print("Average Answer Relevance:", round(avg_ar, 2))