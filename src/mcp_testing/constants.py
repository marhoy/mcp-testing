"""Package constants for mcp_testing."""

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for mcp-testing."""

    model_config = SettingsConfigDict(env_file="config.env")

    # Azure OpenAI settings
    AZURE_OPENAI_ENDPOINT: str = "https://your-endpoint.openai.azure.com/"
    AZURE_OPENAI_API_VERSION: str = "2024-10-21"
    AZURE_LLM_DEPLOYMENT: str = "gpt-4o-mini-2024-07-18"

    # FastAPI settings
    SERVER_BASE_URL: HttpUrl = HttpUrl("http://localhost:8545")
    MCP_MOUNT_PATH: str = "/mcp"


settings = Settings()
