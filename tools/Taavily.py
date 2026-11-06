import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def tavily_search(query: str) -> str:
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise RuntimeError("Set TAVILY_API_KEY in your environment or .env file.")

    client = TavilyClient(api_key=api_key)
    response = client.search(query=query, max_results=5)
    results = []

    for index, result in enumerate(response["results"], start=1):
        title = result.get("title", "unknown")
        url = result.get("url", "")
        snippet = result.get("content", "").strip()
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."
        results.append(f"{index}. **{title}**\n  {url}\n  {snippet}")

    return "\n\n".join(results)
