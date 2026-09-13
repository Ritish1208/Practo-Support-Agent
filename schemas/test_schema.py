from response_schema import AgentResponse

result = AgentResponse(
    query="What is cancellation policy?",
    route="rag",
    response="Patients may cancel appointments..."
)

print(result.model_dump())