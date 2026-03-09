import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def report_agent(idea, research, competitors, opportunities):

    prompt = f"""
    You are a startup strategy consultant.

    Create a structured startup analysis report based on the following information.

    Startup Idea:
    {idea}

    Research:
    {research}

    Competitors:
    {competitors}

    Opportunities:
    {opportunities}

    Provide a clear report with sections:

    1. Market Overview
    2. Key Competitors
    3. Market Opportunities
    4. Suggested Startup Strategy
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content