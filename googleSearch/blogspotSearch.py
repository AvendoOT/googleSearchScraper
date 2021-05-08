from bs4 import BeautifulSoup
import feedparser
import urllib.request
import json


def getSearches(query):
    JSON_FEED_URL = 'http://' + 'sdpinterzlocin' + '.blogspot.com/feeds/posts/default?alt=json'
    json_feed = urllib.request.urlopen(JSON_FEED_URL)
    data = json.load(json_feed)
    pages_count = data["feed"]["openSearch$totalResults"]["$t"]
    print("Total blog entries = " + pages_count)

    pages_batch = 500
    blog_posts = []
    end_index = (int(pages_count) / pages_batch) + 2

    fetch_count = 0
    for counter in range(1, int(end_index)):
        feed_url = 'http://' + 'sdpinterzlocin' + '.blogspot.com/feeds/posts/default?start-index=' + str(
            (counter - 1) * pages_batch + 1) + '&max-results=500'

        fp = feedparser.parse(feed_url)
        for e in fp.entries:
            link = e.links[4].href
            fetch_count = fetch_count + 1
            page = urllib.request.urlopen(link)
            soup = BeautifulSoup(page, from_encoding="utf-8")
            content = soup.get_text()
            blog_posts.append({'title': e.title, 'content': content, 'link': link})

    return blog_posts
