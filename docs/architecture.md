# Practo Support Agent Architecture

User
  ↓
Streamlit UI
  ↓
FastAPI
  ↓
LangGraph Router
 ┌─────────────┬─────────────┐
 ↓             ↓
RAG         Appointment Tool
 ↓             ↓
ChromaDB     MCP Server
 └──────┬──────┘
        ↓
    Response


## Components

### Streamlit UI
Provides the user interface for submitting healthcare support queries and viewing responses.

### FastAPI
Acts as the API layer between the frontend and the agent workflow.

### LangGraph Router
Determines whether a query should be routed to the RAG pipeline or the Appointment Tool.

### RAG Pipeline
Retrieves relevant healthcare policy information from the knowledge base.

### ChromaDB
Stores vector embeddings and performs semantic similarity search.

### Appointment Tool
Handles appointment-specific requests such as appointment status lookup.

### MCP Server
Provides tool access for appointment records and structured appointment information.

### Response Layer
Returns the final response to the user through the Streamlit interface.