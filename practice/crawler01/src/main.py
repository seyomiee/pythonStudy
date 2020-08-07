from flask import Flask, render_template, request, Response
#import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url="https://www.youtube.com/channel/UCYaBl0gtXV_3sHW4bQjq0hA/videos"


'''
div items << div details << a video-title, href
dib container<< div content << a string  //tag
div contents << span string

'''

driver = webdriver.Chrome()
driver.get(url)

elements = driver.find_elements(video-title,'a')
for e in elements:
  print(e.text)



headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

@app.route('/')
def home():
  return hello;

app.run(host="0.0.0.0",debug=TRUE)
