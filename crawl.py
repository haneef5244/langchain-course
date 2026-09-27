

from langchain_tavily import TavilyCrawl
from logger import log_success
from langchain_core.documents import Document

async def crawl_url(url: str): 
    tavily_crawl = TavilyCrawl()

    res = await tavily_crawl.ainvoke({
        "url": url,
        "max_depth": 5,
        "max_breadth": 500,
        "extract_depth": "advanced",
        "instructions": "Find all pages on the LangChain features, functionalities, and documentations."
    })
    all_docs = res["results"]

    results = [Document(page_content=result['raw_content'], metadata={ 'source': result['url']}) for result in all_docs] 

    log_success(
        f"TavilyCrawl: Successfully crawled {len(all_docs)} URLs from {url}"
    )

    return results

# crawl_url(url="https://python.langchain.com")