from agent.router import app

config = {
    "configurable": {
        "thread_id": "demo-thread"
    }
}

result = app.invoke(
    {
        "query":
        "What is the cancellation policy?"
    },
    config=config
)

print(result)