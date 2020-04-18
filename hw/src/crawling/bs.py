import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

'''
목록을 가져온다
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
'''
def extract_table():
  result= requests.get(url)
  soup=BeautifulSoup(result.text, "html.parser")
  country_table= soup.find("tbody")
  country= country_table.find_all("td")

  countries=[]
  arr=[]

  for x in country:
    countries.append(x.string)
    
  for idx, x in enumerate(countries):
    if x=="No universal currency":
      arr.pop()
    elif x== None:
      None
    elif x!="No universal currency":
      arr.append(x)
  return arr

def main():
  country_list= extract_table()
  for idx, x in enumerate(country_list[0::4]):
    print(f"# {idx} {x}")

  try: asw=int((input("#: ")))    
  except:
    print("that wasn't a number.")
  
  print(f"you chose {country_list[asw*4]}. the currency code is {country_list[(asw+1)*3]}")


main()
