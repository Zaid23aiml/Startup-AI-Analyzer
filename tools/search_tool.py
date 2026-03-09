import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query):
    response=tavily.search(query=query,num_results=5)

    results=[]

    for r in response["results"]:
        results.append(r["content"])

    return "\n".join(results)