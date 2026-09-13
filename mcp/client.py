import asyncio
from fastmcp import Client


async def main():

    client = Client("mcp/server.py")

    async with client:

        result1 = await client.call_tool(
            "check_appointment_status",
            {"appointment_id": "APT1001"}
        )

        print("\nREQUEST: APT1001")
        print("RESPONSE:")
        print(result1)

        print("\n" + "=" * 50)

        result2 = await client.call_tool(
            "check_appointment_status",
            {"appointment_id": "APT1002"}
        )

        print("\nREQUEST: APT1002")
        print("RESPONSE:")
        print(result2)


if __name__ == "__main__":
    asyncio.run(main())