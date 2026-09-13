import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(BASE_DIR)


from rag.rag_engine import retrieve_context
from langgraph.graph import StateGraph
from memory.memory_manager import(save_message, load_memory
                                                              )
from typing import TypedDict
from tools.appointment_lookup import get_appointment
from resilience.retry_utils import run_with_retry
from resilience.timeout_utils import run_with_timeout
from utils.logger import logger
class AgentState(TypedDict):
    query : str
    route: str
    response: str
builder = StateGraph(AgentState)
def router(state: AgentState):
    query =  state["query"].lower()

    if "apt" in query:
        return {
            "route": "appointment"

        }
    return {
        "route": "rag"
    }
if __name__== "__main__" :
  print(
    router(
        {
            "query":
            "Show appointment APT1001"
        }
    )
 )
if __name__== "__main__" :
  print(
    router(
        {
            "query":
            "What is the cancellation policy?"
        }
    )
 )

def rag_node(state: AgentState):
    save_message("user",state["query"])
    question = state["query"]

    try:

        context, distance = run_with_retry(
            run_with_timeout,
            retrieve_context,
            question,
            timeout=5
        )
 
        if distance > 1.5:
            logger.info(f"RAG Query : {question}")
            response = ("I could not find reliable information in the healthcare knowledge base.")
            save_message("assistant", response)
            return {
                "response":
                response
            }
        logger.info(f"RAG Query : {question}")
        save_message("assistant", context)
        return {
            "response": context
        }

    except Exception as e:

        return {
            "response":
            f"RAG retrieval failed: {str(e)}"
        }

def appointment_node(state):

    query = state["query"]
    save_message("user", query)
    import re

    match = re.search(
        r"APT\d+",
        query.upper()
    )

    if match:

        appointment_id = match.group()

        result = get_appointment(
            appointment_id
        )

        if not result:
           logger.info(f"Appointment Lookup: {appointment_id}")
           return {
                "response":
                f"No appointment found for {appointment_id}."
            }

        response = (
            f"Appointment ID: {result['record_id']}\n\n"
            f"Status: {result['status']}\n\n"
            f"Category: {result['category']}\n\n"
            f"Consultation Fee: ₹{result['consultation_fee_inr']}\n\n"
            f"Escalation Score: {result['escalation_score']}"
        )
        logger.info(f"Appointment Lookup: {appointment_id}")
        save_message("assistant", response)
        return {
            "response": response
        }
    response=("No appointment ID found in your query.")
    save_message("assistant", response)
    return {
        "response":
       response
    }

    
def route_decision(state: AgentState):
    return state["route"]
graph = StateGraph(AgentState)

graph.add_node("router", router)
graph.add_node(
    "rag",
    rag_node
)
graph.add_node(
    "appointment",
    appointment_node
)
graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "rag": "rag",
        "appointment": "appointment"
    }
)
app = graph.compile()

from schemas.response_schema import AgentResponse
result= app.invoke(
    {
        "query":
        "What is the cancellation policy?"
    }
)

validated = AgentResponse(
    query= result["query"],
    route= result["route"],
    response=result["response"]

)
print(validated.model_dump())

from guardrails.injection_detector import detect_injection
from guardrails.pii_masker import mask_phone_numbers


def guardrail_node(state):

    query = state["query"]

    query = mask_phone_numbers(query)

    if detect_injection(query):

        return {
            "query": query,
            "response":
            "Prompt injection detected."
        }

    return {
        "query": query
    }
def formatter_node(state):

    return {
        "query": state["query"],
        "route": state["route"],
        "response": state["response"]
    }

builder.add_node(
    "guardrail",
    guardrail_node
)

builder.add_node(
    "router",
    router
)

builder.add_node(
    "appointment",
    appointment_node
)

builder.add_node(
    "rag",
    rag_node
)

builder.add_node(
    "formatter",
    formatter_node
)

builder.set_entry_point(
    "guardrail"
)

builder.add_edge(
    "guardrail",
    "router"
)
builder.add_edge(
    "appointment",
    "formatter"
)

builder.add_edge(
    "rag",
    "formatter"
)

builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "rag": "rag",
        "appointment": "appointment"
    }
)
builder.set_finish_point(
    "formatter"
)

from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

conn = sqlite3.connect(
    "checkpoints.sqlite",
    check_same_thread=False
)

memory = SqliteSaver(conn)

app = builder.compile(
    checkpointer=memory
)