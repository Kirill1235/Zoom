import requests
from bs4 import BeautifulSoup
import lxml
def real_time():
    region = 'data-tz="Europe/Moscow"'
    url = "https://time100.ru/Saint-Petersburg"
    page = requests.get(url)
    page.encoding = 'utf-8'
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        s = soup.find("h2")
        return s.find_next().find_next().text
    else:
        return "Error"


print(real_time())







