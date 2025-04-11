"""Define LLM models and their parameters."""

import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain_openai import AzureChatOpenAI

from mcp_testing import config

# Set common environment variables for the Azure OpenAI API
os.environ["AZURE_OPENAI_ENDPOINT"] = config.AZURE_OPENAI_ENDPOINT
os.environ["OPENAI_API_VERSION"] = config.AZURE_OPENAI_API_VERSION

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/",
)


def get_llm() -> AzureChatOpenAI:
    """Get the LLM model for the chatbot."""
    return AzureChatOpenAI(
        azure_deployment=config.AZURE_LLM_DEPLOYMENT,
        azure_ad_token_provider=token_provider,
        temperature=0,
    )
