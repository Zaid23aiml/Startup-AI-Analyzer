import os
from groq import Groq
from dotenv import load_dotenv
from tools.search_tool import search_web

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def competitor_agent(startup_idea):

    search_data = search_web(startup_idea + " competitors startups companies")

    prompt = f"""
    You are a startup market analyst.

    Based on the research data below, identify existing companies or startups
    that could be competitors to the idea: {startup_idea}

    Research Data:
    {search_data}

    Provide:
    - List of competitors
    - Short description of each company
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content