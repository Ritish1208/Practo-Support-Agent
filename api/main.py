from fastapi import FastAPI
from api.models import AskRequest, AskResponse
from agent.router import app as agent_app
from logs.logger import log_request
import time
from guardrails.pii_masker import mask_phone_numbers
from resilience.timeout_utils import (
    run_agent_with_global_timeout
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message":
        "Practo Support Agent Running"
    }


@app.post("/ask")
def ask_agent(request: AskRequest):

    start_time = time.time()

    result = run_agent_with_global_timeout(
        agent_app,
        {
            "query": request.query
        },
        {
            "configurable": {
                "thread_id": "api-thread"
            }
        },
        timeout=15
    )

    duration_ms = int(
        (time.time() - start_time) * 1000
    )

    masked_query = mask_phone_numbers(request.query)
    log_request(
         masked_query,
        result["response"],
        duration_ms
    )

    return AskResponse(
        query=result["query"],
        route=result["route"],
        response=result["response"]
    )