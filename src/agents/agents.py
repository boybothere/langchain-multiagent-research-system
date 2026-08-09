from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

reader_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a research assistant.

Your job is to examine the search results and identify
the single most relevant URL for deeper research.

Return ONLY the URL.

Do not explain your choice.
Do not return markdown.
Do not return anything except the URL."""
    ),

    (
        "human",
        """Topic:

{topic}

Search Results:

{search_results}"""
    )
])


reader_chain = reader_prompt | llm | StrOutputParser()


writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert research writer.

Write clear, structured and insightful reports.

Use ONLY the research provided to you.

Do not invent:
- statistics
- sources
- URLs
- facts

If information is unavailable, clearly say so."""
    ),

    (
        "human",
        """Write a detailed research report on the topic below.

Topic:
{topic}

Research Gathered:
{research}

Structure the report as:

- Introduction
- Key Findings
  - minimum 3 well-explained points
- Conclusion
- Sources
  - list the actual URLs present in the research

Be detailed, factual and professional."""
    )
])


writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a sharp and constructive research critic.

Evaluate the report honestly and specifically.

Pay particular attention to:
- factual support
- quality of evidence
- use of sources
- depth of analysis
- clarity
- actionable recommendations"""
    ),

    (
        "human",
        """Review the research report below and evaluate it strictly.

Report:

{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""
    )
])


critic_chain = critic_prompt | llm | StrOutputParser()