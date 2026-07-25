from dotenv import load_dotenv
from dotenv import dotenv_values
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch
import os

load_dotenv(override=True)


# Using tavilyClient
# tavily = TavilyClient()

# @tool
# def search(query:str) -> str:
#     """
#     Tool that searches over the internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-5")
#tools = [search]
tools = [TavilySearch()]
agent = create_agent(model = llm, tools=tools)

def main():
    print("Hello from langchain-documentationhelper!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job postings for remote AI engineer fulltime positions in linkedin")})
    print(result)
    




if __name__ == "__main__":
    main()
