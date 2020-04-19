import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"
c_url="https://transferwise.com/gb/currency-converter/"

'''
1)목록을 가져온다
정..렬..
/ 번호순서/ 국가이름/

알파벳 순으로 정렬
no universal currency는 제외

-> 입력!
-> 숫자가아니면 that wasn't a number.
-> 맞으면 you chose 어쩌구
        the currency code is 저쩌구
012 3
456 7  

2)
where are you from? choose 넘버
#. 선택
<국가이름>
-> now choose another country.
#. 선택
<국ㄱㅏ이름>

->how many 돈 do you want to covert to krw?
1) 낫넘버
2) 돈 입력 -> 돈 5,000 is 다른돈 2,500

'''

countries = []
answers=[]

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)

def ask():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"#.{choice} {country['name']}")
      answer={"country":country['name'],
      "code":country['code']}
      answers.append(answer)
      
  except ValueError:
    print("That wasn't a number.")
    ask()

def c_result():
  print(f"How many {answers[0].get('code')} do you want to convert to {answers[1].get('code')}?")
  try:
    amount=int(input())
    money=convert_currency(amount)
    r=format_currency(money, answers[1].get('code'))
    print(f"{answers[0].get('code')} {amount} is {r}")
  except ValueError:
    print("that wasn't number.")
    c_result()

def convert_currency(amount):
  one= answers[0].get('code')
  two= answers[1].get('code')
  c_convert = requests.get(c_url + f"{one}-to-{two}-rate?amount={amount}")
  soup = BeautifulSoup(c_convert.text, "html.parser")
  get_currency = soup.find("input", {"id": "cc-amount-to"})
  result= get_currency.get("value")
  return result

def main():
  for index, country in enumerate(countries):
    print(f"#{index} {country['name']}")

  print("where are you from? choose")
  ask()
  print("Now choose another country")
  ask()
  c_result()
  
main()

main()
