from langgraph.graph import StateGraph, END
from typing import TypedDict

from agents.research_agent import research_agent
from agents.competitor_agent import competitor_agent
from agents.opportunity_agent import opportunity_agent
from agents.report_agent import report_agent


class StartupState(TypedDict):
    idea: str
    research: str
    competitors: str
    opportunities: str
    report: str


# Create graph
workflow = StateGraph(StartupState)


# -----------------
# Node Functions
# -----------------

def run_research(state):
    result = research_agent(state["idea"])
    return {"research": result}


def run_competitors(state):
    result = competitor_agent(state["idea"])
    return {"competitors": result}


def run_opportunities(state):
    result = opportunity_agent(state["idea"])
    return {"opportunities": result}


def run_report(state):
    result = report_agent(
        state["idea"],
        state["research"],
        state["competitors"],
        state["opportunities"]
    )
    return {"report": result}


# -----------------
# Add Nodes
# -----------------

workflow.add_node("research_agent", run_research)
workflow.add_node("competitor_agent", run_competitors)
workflow.add_node("opportunity_agent", run_opportunities)
workflow.add_node("report_agent", run_report)


# -----------------
# Define Flow
# -----------------

workflow.set_entry_point("research_agent")

workflow.add_edge("research_agent", "competitor_agent")
workflow.add_edge("competitor_agent", "opportunity_agent")
workflow.add_edge("opportunity_agent", "report_agent")
workflow.add_edge("report_agent", END)


# Compile app
app = workflow.compile()