import requests

my_api_key = "AIzaSyC-BOkYTT5HJVv3cs7vsIQGqYgsuKfOFo0"
my_cse_id = "e6e297083627b8ea2"


def get_searches(query):
    page = 1
    results = []
    while page < 6:
        start = (page - 1) * 10
        query = query.replace(' ', '+')
        url = f"https://www.googleapis.com/customsearch/v1?key={my_api_key}&cx={my_cse_id}&q={query}&start={start}"
        data = requests.get(url).json()
        search_items = data.get("items")

        for i, search_item in enumerate(search_items, start=1):
            title = search_item.get("title")
            snippet = search_item.get("snippet")
            link = search_item.get("link")
            results.append({'title': title, 'content': snippet, 'link': link})
        page += 1
    return results
