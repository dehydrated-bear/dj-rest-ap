from algoliasearch_django import algolia_engine
from algoliasearch.search.client import SearchClientSync

def get_client():
    return algolia_engine.client

def get_index(index_name='cfe_Product'):
    # client=get_client()
    
    client = SearchClientSync("3WLH0WVDSM", "3a0976bb3b5096dfe0a86287838fb4f7")
    index=client.search_single_index(
    index_name=index_name,)
   
    return index

def perform_search(query,**kwargs):
#     client = SearchClientSync("3WLH0WVDSM", "3a0976bb3b5096dfe0a86287838fb4f7")

#     response = client.search(
#     search_method_params={
#         "requests": [
#             {
#                 "indexName": "cfe_Product",
#                 "query": query,
#                 "hitsPerPage": 50,
#             },
#         ],
#     },
# )
    
    
    
    index=get_index()
    results=index
    return results





