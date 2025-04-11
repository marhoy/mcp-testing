"""The FastAPI app with MCP support."""

import random

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from loguru import logger

from mcp_testing import config

app = FastAPI(
    title="FastAPI with MCP",
    description="FastAPI with MCP support",
    version="0.1.0",
)


@app.post("/earthquake_probability")
async def earthquake_probability(location: str) -> float:
    """For a given location, return the earthquake probability."""
    logger.info(f"Calculating earthquake probability for {location}")
    return random.uniform(0, 1)  # noqa: S311


@app.post("/next_volcanic_eruption")
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


# Create an MCP server from the FastAPI app
mcp = FastApiMCP(
    app,
    # Optional parameters
    name="My API MCP",
    description="My API description",
    base_url=config.SERVER_BASE_URL.unicode_string(),
)

# Mount the MCP server inside the FastAPI app
mcp.mount(mount_path=config.MCP_MOUNT_PATH)


def main() -> None:
    """Run the FastAPI application with MCP support."""
    import uvicorn

    uvicorn.run(
        app,
        host=config.SERVER_BASE_URL.host or "localhost",
        port=config.SERVER_BASE_URL.port or 8080,
    )


if __name__ == "__main__":
    # For debugging purposes, we can run the server directly
    main()
