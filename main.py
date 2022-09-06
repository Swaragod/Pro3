import requests
import bs4
from pprint import pprint
from fake_user_agent import user_agent

ua = user_agent()
pprint(ua)
url = "https://habr.com/ru/all/"


KEYWORDS = ['дизайн', 'фото', 'web', 'python','Big Data', 'Машинное обучение']

response = requests.get(url, headers=ua)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")

# pprint(soup)

articles = soup.find_all("article")
pprint(articles)

for article in articles:
    keywords = article.find_all(class_="tm-article-snippet__hubs-item")
    keywords = [keyword.text.strip() for keyword in keywords]
    pprint(keywords)
    print()