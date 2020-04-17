import requests
'''
반가워 어쩌구 
주소 입력 
-> 
  1) http ?
  2) 적합한 주소?
    -> up/down
-> 게임 또 할거야?
'''

def restart():
  q=input("Do you want to start over? y/n ")
  if q=="y":
    main()
  else:
    print("bye")
    return

def main():
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  urls= input().split(",")
  for x in urls:
    x= x.strip()
    if  "." not in x:
       print("not valid url")
    elif "http" not in x:
      x=f"http://{x}"
    r = requests.get(f'{x}')
    if r.status_code == 200:
      print(f"{x} ,up")
    else:
      print(f"{x} ,down")
  restart()
     

main()
  