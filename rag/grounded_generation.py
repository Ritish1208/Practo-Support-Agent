from rag_engine import retrieve_context

THRESHOLD = 1.3


def answer_question(question):

    context, distance = retrieve_context(
        question
    )

    if distance > THRESHOLD:

        return (
            "I don't know based on the "
            "available knowledge base."
        )

    return context


question = "Who won IPL 2024?"

answer = answer_question(
    question
)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)