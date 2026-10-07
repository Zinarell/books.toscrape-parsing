st_accept = "text/html" # говорим веб-серверу, 
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

# импортируем модуль
import requests
# отправляем запрос с заголовками по нужному адресу
req = requests.get("http://books.toscrape.com/", headers)

src = req.text


# импортируем модуль
from bs4 import BeautifulSoup
# инициализируем html-код страницы 
soup = BeautifulSoup(src, 'lxml')
# считываем заголовок страницы
title = soup.title.string
print(title)


books = soup.find_all("article", class_="product_pod")
for book in books[:10]:
    book_title = book.h3.a.attrs["title"]
    print(book_title)
