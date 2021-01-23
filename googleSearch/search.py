from googleapiclient.discovery import build

my_api_key = "AIzaSyC-BOkYTT5HJVv3cs7vsIQGqYgsuKfOFo0"
my_cse_id = "e6e297083627b8ea2"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    print(res)
    return res['items']


def getSearches(query):
    i = 0
    results = []
    while i < 70:
        result = google_search(query, my_api_key, my_cse_id, num=10, start=i)
        i += 10
        for r in result:
            results.append({
                'title': r['title'],
                'link': r['link']
            })
    return results
