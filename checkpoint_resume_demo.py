from langgraph.graph import StateGraph
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from typing import TypedDict

class DemoState(TypedDict, total=False):
    stop_after_node2: bool


# Node 1
def node1(state):
    print("NODE 1 EXECUTED")
    return state


# Node 2
def node2(state):
    print("NODE 2 EXECUTED")

    if state.get("stop_after_node2", False):
        print("SIMULATED INTERRUPTION AFTER NODE 2")
        raise Exception("Manual Stop")

    return state


# Node 3
def node3(state):
    print("NODE 3 EXECUTED")
    return state


# SQLite checkpoint
conn = sqlite3.connect(
    "demo_checkpoints.sqlite",
    check_same_thread=False
)

memory = SqliteSaver(conn)

builder = StateGraph(DemoState)

builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)

builder.set_entry_point("node1")

builder.add_edge("node1", "node2")
builder.add_edge("node2", "node3")

builder.set_finish_point("node3")

app = builder.compile(
    checkpointer=memory
)

config = {
    "configurable": {
        "thread_id": "demo-thread"
    }
}

print("===== RUN 1 =====")

try:
    app.invoke(
        {
            "stop_after_node2": True
        },
        config=config
    )
except Exception:
    print("RUN INTERRUPTED")

print("\n===== RUN 2 =====")

app.update_state(
    config,
    {
        "stop_after_node2": False
    }
)

result = app.invoke(
    None,
    config=config
)

print(result)