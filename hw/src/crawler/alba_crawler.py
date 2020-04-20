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
  #print(title.text)
  with open(f"{title.text}.csv", mode="w") as file:
    writer= csv.writer(file)
    writer.writerow(["place","title","time","pay","date"])
    req = requests.get(row.a['href']) #브랜드 별 주소 가져오기
    soup = bs(req.text, 'html.parser')
    detail= soup.find('tbody')
    for row in detail:
      if row ==None
      
        place= row.find('td',{'class':'local'})
        print(place)