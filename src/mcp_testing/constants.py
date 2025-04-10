"""Package constants for mcp_testing."""

from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for mcp-testing."""

    # Azure OpenAI settings
    AZURE_OPENAI_ENDPOINT: str = "https://smuod-openai-sweden.openai.azure.com/"
    AZURE_OPENAI_API_VERSION: str = "2024-10-21"
    AZURE_LLM_DEPLOYMENT: str = "gpt-4o-mini-2024-07-18"

    # FastAPI settings
    SERVER_URL: HttpUrl = HttpUrl("http://localhost:8543/sse")


settings = Settings()
