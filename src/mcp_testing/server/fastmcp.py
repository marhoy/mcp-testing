"""A simple FastMCP server."""

import random

from loguru import logger
from mcp.server.fastmcp import FastMCP

from mcp_testing import config

mcp = FastMCP("MCP Demo")


@mcp.tool()
async def earthquake_probability(location: str) -> float:
    """For a given location, return the earthquake probability."""
    logger.info(f"Calculating earthquake probability for {location}")
    return random.uniform(0, 1)  # noqa: S311


@mcp.tool()
async def next_volcanic_eruption() -> str:
    """Get the location of the next volcanic eruption."""
    logger.info("Getting the location of the next volcanic eruption")
    options = [
        "Campi Flegrei (Italy)",
        "Mt. Vesuvius (Italy)",
        "Cumbre Vieja (La Palma, Canary Islands)",
        "Mount St. Helens (Washington, United States)",
        "Popocatépetl (Mexico)",
        "Yellowstone Supervolcano (Wyoming, United States)",
    ]
    return random.choice(options)  # noqa: S311


def main() -> None:
    """Run the FastMCP server."""
    mcp.settings.host = config.SERVER_BASE_URL.host or "localhost"
    mcp.settings.port = config.SERVER_BASE_URL.port or 8080
    mcp.settings.sse_path = config.MCP_MOUNT_PATH
    mcp.run(transport="sse")
