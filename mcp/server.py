import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(BASE_DIR)


from fastmcp import FastMCP

from tools.appointment_lookup import get_appointment

mcp = FastMCP(
    "Practo Appointment MCP Server"
)

@mcp.tool
def check_appointment_status(
    appointment_id: str
):
    """
    Returns appointment status,
    consultation fee and
    escalation score.
    """
    return get_appointment(
        appointment_id
    )

if __name__ == "__main__":
    mcp.run()