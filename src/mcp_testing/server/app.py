"""The FastAPI app with MCP support."""

import random

from fastapi import FastAPI
from fastapi_mcp import add_mcp_server
from loguru import logger
from pydantic import BaseModel, Field

app = FastAPI(
    title="MCP FastAPI",
    description="FastAPI with MCP support",
    version="0.1.0",
)


class DetentionProbabilityRequest(BaseModel):
    """Request model for vessel detention probability."""

    vessel_id: str = Field(..., description="The ID of the vessel")


class DetentionProbabilityResponse(BaseModel):
    """Response model for vessel detention probability."""

    probability: float = Field(
        ..., description="The probability that the vessel will be detained"
    )


@app.post("/detention_probability")
async def vessel_probability(
    vessel_id: str,
) -> float:
    """Return the probability that a vessel will be detained by Port State Control."""
    logger.info("Processing request /detention_probability")
    return random.random()  # noqa: S311


mcp_server = add_mcp_server(
    app,
    mount_path="/mcp",
    name="MCP-testing API",
)


# Optionally, you can add custom MCP tools not based on FastAPI endpoints
@mcp_server.tool()
async def get_vessel_count() -> int:
    """Get the total number of vessels in the database."""
    return random.randint(500, 1000)  # noqa: S311


# Run the server if this file is executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5050)
