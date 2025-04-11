"""Functions for communicating with the MCP server."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from urllib.parse import urljoin

from langchain_mcp_adapters.client import BaseTool, MultiServerMCPClient, SSEConnection

from mcp_testing import config


@asynccontextmanager
async def get_mcp_tools(mcp_url: str | None = None) -> AsyncGenerator[list[BaseTool]]:
    """Get the MCP tools to be used by an agent."""
    # Create a connection to the MCP server using SSE
    if mcp_url is None:
        mcp_url = urljoin(
            config.SERVER_BASE_URL.unicode_string(), config.MCP_MOUNT_PATH
        )
    my_mcp_server_1 = SSEConnection(
        transport="sse",
        url=mcp_url,
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
