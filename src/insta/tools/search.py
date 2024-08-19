import requests
import json
import os

from langchain.tools import tool

class SearchTools:

    @tool('search_internet')
    def search_internet(query: str) -> str:
        """
        Use this tool to search the internet for information. 
        This tool returns 5 results from Google search engine
        """
        return SearchTools.search(query)
    
    @tool('search_instagram')
    def search_instagram(query: str) -> str:
        """
        Use this tool to search Instagram. This tool returns 5 results from Instagram pages.
        """
        return SearchTools.search

    def search(query, limit=5):

        url = "https://google.serper.dev/search"
        
        payload = json.dumps({
            "q": query,
            "num": limit,
        })

        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
        }

        response = requests.request("Post", url=url, headers=headers, data=payload)
        results = response.json()["organic"]
        string = []

        for result in results:
            string.append(f"{result['title']}\n{result['snippet']}\n{result['url']}\n")

        return f"Search results for '{query}':\n\n" + "\n".join(string)
