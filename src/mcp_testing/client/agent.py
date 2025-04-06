from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from mcp_testing.client.llm_models import get_llm

llm = get_llm()


def get_agent():
    with MultiServerMCPClient(
        {
            "detention": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:5000/mcp",
                "transport": "sse",
            }
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())

        yield agent


#    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
#    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
