from turtle import title
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody",{"class" : "lister-list"}).find_all("tr", limit=10)
count = 1

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    rate = tr.find("td",{"class":"ratingColumn"}).find("strong").text
    print(f"{count}- {title.ljust(50)}  Yapım Yılı: {year}   İMDB: {rate}")
    count +=1

