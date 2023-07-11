from bs4 import BeautifulSoup
import ipdb
import requests

    # ap.select("span.PagePromoContentIcons-text")
    # ap.select("a.href")
    # ap.select("div.PagePromo-description")
    # ap.select("li.PageList-items-item a")

def create_ap_dict(): 
    headers = {'user-agent': 'my-app/0.0.1'}
    html = requests.get("https://apnews.com/", headers=headers)

    ap = BeautifulSoup(html.text, 'html.parser')
    articles = {}


    for article in ap.select("li.PageList-items-item"):
        headline = article.select("a")[0].text

        articles[headline] = {
            'article_link': article.select("a")[0]["href"]
        }

    return articles

articles = create_ap_dict()
print(articles)