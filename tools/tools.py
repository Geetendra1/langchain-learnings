from langchain import SerpAPIWrapper
import os
# serpapi = SerpAPIWrapper()


# class CustomSerpAPIWrapper(SerpAPIWrapper):
#     def __init__(self):
#         super(CustomSerpAPIWrapper, self).__init__()

#     @staticmethod
#     def _process_response(res: dict) -> str:
#         """Process response from SerpAPI."""
#         if "error" in res.keys():
#             raise ValueError(f"Got error from SerpAPI: {res['error']}")
#         if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
#             toret = res["answer_box"]["answer"]
#         elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
#             toret = res["answer_box"]["snippet"]
#         elif (
#             "answer_box" in res.keys()
#             and "snippet_highlighted_words" in res["answer_box"].keys()
#         ):
#             toret = res["answer_box"]["snippet_highlighted_words"][0]
#         elif (
#             "sports_results" in res.keys()
#             and "game_spotlight" in res["sports_results"].keys()
#         ):
#             toret = res["sports_results"]["game_spotlight"]
#         elif (
#             "knowledge_graph" in res.keys()
#             and "description" in res["knowledge_graph"].keys()
#         ):
#             toret = res["knowledge_graph"]["description"]
#         elif "snippet" in res["organic_results"][0].keys():
#             toret = res["organic_results"][0]["link"]

#         else:
#             toret = "No good search result found"
#         return toret


def get_profile_url(name: str) -> str:
    """Searches for twitter Profile Page."""
    serpapi_api_key=os.environ.get("SERPAPI_API_KEY")
    print("serpapi_api_key",serpapi_api_key)
    search = SerpAPIWrapper(serpapi_api_key="7e472711da9de75808b39e3ce9f771a6c18f51dd6f17d89015ea9a4d05482a06")
    res = search.run(f"{name}")
    return res

