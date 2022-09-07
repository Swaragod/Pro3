import requests
import bs4
from fake_headers import Headers

HEADERS = Headers(os="mac", headers=True).generate()
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'В']

url = "https://habr.com/ru/all/"
url_base = "https://habr.com"

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")
for article in articles:
    previews = article.find_all(class_="tm-article-body tm-article-snippet__lead")
    previews = [preview.text.strip() for preview in previews]
    for preview in previews:
        for keyword in KEYWORDS:
            if keyword in preview:
                post_date = article.find("time").attrs["title"][0:10]
                title = article.find("h2").find("span").text
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                link = url_base + href
                print(f'<{post_date}> - <{title}> - <{link}>')


