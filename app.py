import streamlit as st
from graph.workflow import app

st.set_page_config(page_title="Startup AI Analyzer", page_icon="🚀")

st.title("🚀 AI Startup Idea Analyzer")
st.write("Analyze your startup idea using a multi-agent AI system.")

idea = st.text_input("Enter your startup idea")

if st.button("Analyze Idea"):

    if idea.strip() == "":
        st.warning("Please enter a startup idea")
    else:
        with st.spinner("Agents analyzing your idea..."):

            result = app.invoke({
                "idea": idea
            })

        st.success("Analysis complete!")

        st.subheader("📊 Startup Analysis Report")
        st.write(result["report"])