from langchain_community.tools.tavily_search.tool import TavilySearchResults


from langchain_community.tools.tavily_search import TavilySearchResults

tools: list[TavilySearchResults] = [TavilySearchResults(max_results=1)]