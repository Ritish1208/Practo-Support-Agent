# Checkpoint Demonstration

## Run 1 (Interrupted)

Output:

NODE 1 EXECUTED
NODE 2 EXECUTED
SIMULATED INTERRUPTION AFTER NODE 2
RUN INTERRUPTED

Result:

Execution stopped before graph completion.
The checkpoint was persisted to SQLite using SqliteSaver.

---

## Run 2 (Resume)

Output:

NODE 2 EXECUTED
NODE 3 EXECUTED

Result:

Node 1 was not executed again, demonstrating that previously completed work was restored from the checkpoint.

The graph resumed using the same thread ID and completed successfully.

Thread ID:

demo-thread

Checkpoint Store:

demo_checkpoints.sqlite

## Conclusion

SQLite checkpointing was successfully integrated into the LangGraph workflow using SqliteSaver.

The graph was interrupted after partial execution and later resumed using the same thread ID. During recovery, Node 1 was restored from the checkpoint and was not re-executed, demonstrating persistence of graph state across runs.

This implementation provides fault tolerance and enables recovery from interruptions without restarting the entire workflow.