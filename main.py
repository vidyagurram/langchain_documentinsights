from dotenv import load_dotenv
from dotenv import dotenv_values
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field
import os

load_dotenv(override=True)

class Source(BaseModel):
    """Schema for the source used by an agent"""
    url:str=Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for the Agent response with answer and sources"""
    answer:str=Field(description="The agents answer to the query")
    sources:List[Source]=Field(default_factory=list, description="List of sources used to generate the answer")



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
agent = create_agent(model = llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-documentationhelper!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job postings for remote AI engineer fulltime positions in linkedin")})
    print(result)
    




if __name__ == "__main__":
    main()
