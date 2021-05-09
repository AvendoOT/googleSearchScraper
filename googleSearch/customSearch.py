import requests
from bs4 import BeautifulSoup


def get_searches(query):
    originalQuery = query
    results = []

    # LIKA-ONLINE.COM
    page_num = 1
    query = query.replace('č', '%C4%8D')
    query = query.replace('ć', '%C4%87')
    query = query.replace(' ', '+')
    while page_num < 6:
        url = f"https://www.lika-online.com/page/{page_num}/?s={query}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        job_elems = soup.find_all('div', class_='tdb_module_loop td_module_wrap td-animation-stack')
        for job_elem in job_elems:
            title = job_elem.find('a')['title']
            link = job_elem.find('a')['href']
            results.append({'title': title, 'content': 'snippet', 'link': link})
        page_num += 1

    # LIKAPLUS.HR
    query = originalQuery.replace(' ', '%20')
    query = query.replace('č', '%E8')
    query = query.replace('ć', '%E6')
    url = f"http://www.likaplus.hr/Search.aspx?pojam={query}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elems = soup.find_all('div', class_='clanak')
    for job_elem in job_elems:
        link = job_elem.find('a')['href']
        title = job_elem.find('img')['alt']
        full_link = 'http://www.likaplus.hr' + link
        results.append({'title': title, 'content': 'snippet', 'link': full_link})

    # SLOBODARI.COM
    query = originalQuery.replace(' ', '+')
    query = query.replace('č', '%C4%8D')
    query = query.replace('ć', '%C4%87')
    url = f"https://slobodari.com/?s={query}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elems = soup.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')
    for job_elem in job_elems:
        title = job_elem.find('a')['title']
        link = job_elem.find('a')['href']
        results.append({'title': title, 'content': 'snippet', 'link': link})

    # PROMISE.HR
    query = originalQuery.replace(' ', '+')
    query = query.replace('č', '%C4%8D')
    query = query.replace('ć', '%C4%87')
    url = f"http://promise.hr/?s={query}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elems = soup.find('div', class_='blog-block-1 search-results')
    job_elems = job_elems.find_all('div', class_='post-item')
    for job_elem in job_elems:
        link = job_elem.find('a')['href']
        results.append({'title': 'PROMISE.HR', 'content': 'snippet', 'link': link})

    # GSPRESS.NET
    page_num = 1
    query = originalQuery.replace(' ', '+')
    query = query.replace('č', '%C4%8D')
    query = query.replace('ć', '%C4%87')
    while page_num < 5:
        url = f"https://www.gspress.net/page/{page_num}/?s={query}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        job_elems = soup.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')
        for job_elem in job_elems:
            title = job_elem.find('a')['title']
            link = job_elem.find('a')['href']
            results.append({'title': title, 'content': 'snippet', 'link': link})
        page_num += 1
    return results
