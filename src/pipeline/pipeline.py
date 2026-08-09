from src.tools.tools import web_search, scrape_url
from src.agents.agents import (
    reader_chain,
    writer_chain,
    critic_chain
)


def run_research_pipeline(topic: str) -> dict:

    state = {}
    print("\n" + "=" * 50)
    print("step 1 - search agent is working ...")
    print("=" * 50)

    search_results = web_search.invoke({
        "query": topic
    })

    state["search_results"] = search_results

    print(
        "\nsearch result:\n",
        state["search_results"]
    )


    print("\n" + "=" * 50)
    print("step 2 - reader agent is selecting top resource ...")
    print("=" * 50)

    selected_url = reader_chain.invoke({
        "topic": topic,
        "search_results": state["search_results"]
    })

    selected_url = selected_url.strip()

    print(
        "\nselected URL:\n",
        selected_url
    )


    print("\n" + "=" * 50)
    print("step 3 - scraping selected resource ...")
    print("=" * 50)

    scraped_content = scrape_url.invoke({
        "url": selected_url
    })

    state["scraped_content"] = scraped_content

    print(
        "\nscraped content:\n",
        state["scraped_content"]
    )

    print("\n" + "=" * 50)
    print("step 4 - writer is drafting the report ...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n"
        f"{state['search_results']}\n\n"

        f"SELECTED SOURCE:\n"
        f"{selected_url}\n\n"

        f"DETAILED SCRAPED CONTENT:\n"
        f"{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print(
        "\nFinal Report:\n",
        state["report"]
    )


    print("\n" + "=" * 50)
    print("step 5 - critic is reviewing the report ...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print(
        "\nCritic Report:\n",
        state["feedback"]
    )


    return state