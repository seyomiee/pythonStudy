import os
import csv
import requests
from bs4 import BeautifulSoup as bs

# place, title, time, pay, date

os.system("clear")
alba_url = "http://www.alba.co.kr"

request= requests.get(alba_url)
soup= bs(request.text,"html.parser")
alba_list= soup.find_all('li', {'class': 'impact'})
for row in alba_list:
  title = row.find('span', {'class': 'company'})
  print(title.text)
  with open(f"{title.text}.csv", mode="w") as file:
    writer= csv.writer(file)
    writer.writerow(["place","title","time","pay","date"])
    req = requests.get(row.a['href']) #브랜드 별 주소 가져오기
    soup = bs(req.text, 'html.parser')
    detail= soup.find("div", id="NormalInfo").find("tbody")
    for row in detail.find_all('tr', {"class": ""}):
      if row.td.text != "해당 조건/분류에 일치하는 채용정보가 없습니다.":
        place= row.find('td',{'class':'local'}).text
        print(place)
        title= row.find('td', {'class': 'title'}).text
        time= row.find('td', {'class': 'data'}).text
        pay= row.find('td', {'class': 'pay'}).text
        date= row.find('td', {'class': 'regDate'}).text
        writer.writerow([place, title, time, pay, date])