"""Functions for communicating with the MCP server."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from langchain_mcp_adapters.client import BaseTool, MultiServerMCPClient, SSEConnection

from mcp_testing import config


@asynccontextmanager
async def get_mcp_tools(url: str | None = None) -> AsyncGenerator[list[BaseTool]]:
    """Get the MCP tools to be used by an agent."""
    # Create a connection to the MCP server using SSE
    my_mcp_server_1 = SSEConnection(
        transport="sse",
        url=config.MCP_SERVER_URL.unicode_string() if url is None else url,
        headers=None,
        timeout=10,
        sse_read_timeout=10,
        session_kwargs=None,
    )

    async with MultiServerMCPClient(
        {
            "my_mcp_server_1": my_mcp_server_1,
        }
    ) as client:
        mcp_tools = client.get_tools()
        yield mcp_tools
