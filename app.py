import streamlit as st
from src.pipeline.pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Multi-Agent Research Assistant")
st.caption("Search → Read → Scrape → Write → Critique, powered by Groq + Tavily")

with st.sidebar:
    st.header("About")
    st.write(
        "This app runs a 5-agent pipeline:\n\n"
        "1. **Search** the web (Tavily)\n"
        "2. **Reader** picks the best URL\n"
        "3. **Scrape** that page\n"
        "4. **Writer** drafts a structured report\n"
        "5. **Critic** scores and reviews it"
    )
    st.divider()
    st.write("Requires `GROQ_API_KEY` and `TAVILY_API_KEY` in your `.env` file.")

if "state" not in st.session_state:
    st.session_state.state = None

topic = st.text_input(
    "Research topic",
    placeholder="e.g. Impact of AI agents on software engineering jobs"
)

run = st.button("Run research", type="primary", disabled=not topic.strip())

if run:
    st.session_state.state = None
    try:
        with st.spinner("Running the research pipeline (search → read → scrape → write → critique)..."):
            result = run_research_pipeline(topic)
        st.session_state.state = result
        st.success("Pipeline complete")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

state = st.session_state.state

if state:
    tab_report, tab_critique, tab_research = st.tabs(
        ["📄 Report", "🧐 Critic Feedback", "🗂️ Raw Research"]
    )

    with tab_report:
        st.markdown(state["report"])
        st.download_button(
            "Download report (.md)",
            data=state["report"],
            file_name="research_report.md",
            mime="text/markdown"
        )

    with tab_critique:
        st.markdown(state["feedback"])

    with tab_research:
        st.subheader("Selected source")
        st.write(state.get("selected_url", "N/A"))

        st.subheader("Search results")
        st.text(state["search_results"])

        st.subheader("Scraped content")
        st.text(state["scraped_content"][:3000])