# Multi-Agent Research Assistant

An AI-powered research assistant built with **LangChain, Groq, and Tavily**.

The system takes a research topic, searches the web for relevant information, gathers additional content, generates a structured research report, and evaluates the final report using a critic.

**[Try the Live Demo](https://langchain-multiagent-research-system.onrender.com/)**

## Architecture

The pipeline consists of:

1. **Search Agent**
   - Uses Tavily web search.
   - Finds recent and relevant sources for the given topic.

2. **Reader**
   - Selects relevant sources and retrieves additional information.

3. **Research Writer**
   - Generates a structured research report from the gathered information.

4. **Critic**
   - Reviews the generated report.
   - Provides a score, strengths, weaknesses, and an overall verdict.

## Tech Stack

- Python
- LangChain
- Groq
- Tavily
- LLM-based agents and chains

## Pipeline

```text
Research Topic
      ↓
 Search Agent
      ↓
 Web Search
      ↓
 Source Selection / Reading
      ↓
 Research Writer
      ↓
 Research Report
      ↓
 Critic
      ↓
 Final Evaluation
