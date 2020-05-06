from flask import Flask, render_template, request, Response
import requests
from bs4 import BeautifulSoup

app = Flask('jobs')

@app.route('/')
def home():
  return render_template('home.html')

app.run(host="0.0.0.0", debug=True)