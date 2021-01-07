# Import packages
import os
import urllib
from urllib import response
from urllib.request import urlopen
import requests
from requests.exceptions import ConnectionError
import urllib.request
from bs4 import BeautifulSoup

##### Projenin çözdüğü problemlerin farklı durumları varsa,
# yazdığınız kodun her zaman o durumları karşılayabilecek şekilde olması tercih edilmelidir.
# Fakat bu projede kitabın içeriğine tek sayfa ile erişebildiğimizi kabul edeceğiz.
# Yani programın Wikibooks’taki bitmiş olan kitaplarda çalışması yeterlidir
# ve bu noktada printable versiyonunun hepsinde olduğu varsayılmıştır.
# Eğer bir kitabın printable versiyonu yok ise, programınızın o kitap için çalışmasına gerek yok.########

## Önemli not: Your program should ask the user, how many word frequencies they wish to see (in this
# document, as you can see, 20 words per list has been shown). You can take 20 as your default number
# if the user does not enter a specific number they wish to use.
#### Bu programda eksik, kullanıcının kaç frequencies istediği sorulmalı.


book_1 = input("Enter the first book name: ")
book_1 = book_1.replace(" ", "_")
book_1 = book_1.replace("'", "%27")


url=(f'https://en.wikibooks.org/wiki/{book_1}/Print_version')


try:
    request = requests.get(url)
except ConnectionError:
    print('Web site does not exist')
else:
    print('Web site exists')
    print(request.status_code)
    if request.status_code == 200:
        source = urlopen(url).read()
        # Make a soup
        soup = BeautifulSoup(source, "html.parser")
        # Extract the plain text content from paragraphs
        text = ''
        for paragraph in soup.find_all('p'):
            text += paragraph.text


        with open(f'{book_1}.txt', "w", encoding='utf-8') as file:
            file.write(str(text))

    else:
        print("There is no printable version of this book, please try another book!")



