import os
from groq import Groq
from dotenv import load_dotenv
from tools.search_tool import search_web

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def research_agent(startup_idea):
    search_data=search_web(startup_idea)

    prompt=f"""
    You are a startup research analyst.

    Analyze the following research data and summarize key insights
    about the startup idea: {startup_idea}

    Research Data:
    {search_data}

    Provide:
    - Market overview
    - Industry trends
    """

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
    )

    return response.choices[0].message.content