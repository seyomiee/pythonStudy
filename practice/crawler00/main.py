from flask import Flask, render_template, request, Response
import requests
from bs4 import BeautifulSoup

'''
https://ranking.rakuten.co.jp/weekly/gender={gender}/p={page}/
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}
'''
gender ={
  'femal','male'
}
'''

app = Flask('rank')

ranking=[]

def search_ranking(rank_list):
  for item in rank_list:
      name= item.find('div',{'class': 'rnkRanking_itemName' }).string
      print('⛱')
      print(name)

def rank():
  req= requests.get("https://ranking.rakuten.co.jp/daily/gender=female/p=1/",headers=headers)
  if req:
    soup= BeautifulSoup(req.text,'html5lib')
    main= soup.find_all('div',{'class':'rnkRankingMain'})
    '''
    pager= soup.find('div',{'class':'pager'})
    pages= pager.find_all('span',{'class':'pageDisp'})
    
    num_page=[]
    for a in pages:
      num_page.append(a.string)
      #page 수 만큼 for문,,
    
    for i,index in enumerate(num_page[:-2]):
      print(i, index)
    '''
    #1,2,3위
    #4위 이하
    #ranking_before=soup.find_all('div', {'class':'rnkRanking_top3box'})
    if main:
      ranking_after= main.find_all('div', {'class':'rnkRanking_after4box'})
      print(ranking_after)
      #search_ranking(ranking_before)
      #search_ranking(ranking_after)



  




'''
@app.route('/')
def home():
  return render_template('home.html',age=age,gender=gender)

@app.route('/result')
def result():
  for item in gender:
    g=request.args.get(item)
    print(g)
    #a= request.args.get(age)
    #if g:
    
  return render_template('result.html',g=g)

'''

rank()

app.run(host="0.0.0.0")

