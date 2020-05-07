from flask import Flask, render_template, request, Response
import requests
from bs4 import BeautifulSoup

'''
https://ranking.rakuten.co.jp/daily/gender={gender}/p={page}/
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

def rank():
  r= requests.get("https://ranking.rakuten.co.jp/daily/gender=female/p=1/",headers=headers)
  soup= BeautifulSoup(r.text,'html5lib')
  pager= soup.find('div',{'class':'pager'})
  pages= pager.find_all('a')
  num_page=[]
  for a in pages:
    num_page.append(a.find('span').string)
  print(num_page[:-2])

rank()

app = Flask('rankings')

@app.route('/')
def home():
  return render_template('home.html')

app.run(host="0.0.0.0", debug=True)