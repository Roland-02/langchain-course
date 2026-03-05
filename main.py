from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily_search import TavilySearch


from pydantic import BaseModel, Field
from typing import List

class SearchResult(BaseModel):
    title: str = Field(description="The title of the search result")
    url: str = Field(description="The URL of the search result")
    snippet: str = Field(description="A short snippet of the search result")


load_dotenv()

@tool
def search(query: str) -> str:
    """Search the web for information"""
    print(f"Searching the web for {query}")
    return "This is a test search result"


llm = ChatOllama(model="gemma3:270m", temperature=0)
# tools = [TavilySearch()] # Tavily is built-in tool for searching the web
tools = [search] # Custom search tool
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"input": "What is the capital of France?"})
    print(result)

if __name__ == "__main__":
    main()
