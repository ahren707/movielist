import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
films_website = response.text

soup = BeautifulSoup(films_website, "html.parser")

titles = [title.text for title in soup.findAll(name="h3", class_="title")]

titles.reverse()

with open("list.txt", "w") as file:
    for item in titles:
        file.write(item+"\n")
