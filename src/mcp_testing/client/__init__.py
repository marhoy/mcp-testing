"""Expose client functions."""

from mcp_testing.client.llm_models import get_llm
from mcp_testing.client.mcp_connections import get_mcp_tools

__all__ = ["get_llm", "get_mcp_tools"]
