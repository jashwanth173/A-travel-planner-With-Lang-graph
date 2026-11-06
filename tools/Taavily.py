
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key = os.getenv("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")
)

def tavily_search(query):
    response = client.search()
    query = qyery,
    max_result = 5
    result = []
    for i in enumerate(response["results"],1):
        title = r.get("title","unknown")
        url = r.get("url","")
        snippet = r.get("content","").strip()
        if len(snippet)>300:
            snippent = snippent[:300].rsplit(" ")[0] + "..."
            results.append(f"|{i}.**{title}**\n  {url}\n {snippet}")
            return "\n\n".join(results) 