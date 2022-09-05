import requests
import bs4
from kiss_headers import parse_it

url = "https://habr.com/ru/all/"

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(url)
headers = parse_it(response)
headers.content_type.charset  # output: ISO-8859-1

text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
print(headers)