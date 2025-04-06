"""Define LLM models and their parameters."""

import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain_openai import AzureChatOpenAI

# Set common environment variables for the Azure OpenAI API
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://smuod-openai-sweden.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] = "2024-10-21"

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/",
)


def get_llm() -> AzureChatOpenAI:
    """Get the LLM model for the chatbot."""
    return AzureChatOpenAI(
        azure_deployment="gpt-4o-mini-2024-07-18",
        azure_ad_token_provider=token_provider,
        temperature=0,
    )
