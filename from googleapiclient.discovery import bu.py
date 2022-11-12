from googleapiclient.discovery import build
my_api_key = "AIzaSyBSivYh2u6ZaqRbWL6kebQaoX_b7GcfnHk"
my_cse_id = "a3f58c06f77e94ab6"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res
print (google_search('coffee', 'AIzaSyBSivYh2u6ZaqRbWL6kebQaoX_b7GcfnHk', 'AIzaSyBSivYh2u6ZaqRbWL6kebQaoX_b7GcfnHk'))