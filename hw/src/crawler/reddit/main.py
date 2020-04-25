from flask import Flask, render_template, request
from scrapper import aggregate_subreddits, scrape_subreddit

app = Flask("RedditNews")

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

@app.route("/")
def home():
  return render_template("home.html", subreddits=subreddits)


@app.route("/read")
def read():
  selected = []
  for subreddit in subreddits:
    if subreddit in request.args:
      selected.append(subreddit)
  posts = aggregate_subreddits(selected)
  posts.sort(key=lambda post: post['votes'], reverse=True)
  return render_template("read.html", selected=selected, posts=posts)

'''
@app.route('/read')
def read():
  for subreddit in subreddits:
    reddits=[]
    word= request.args.get(subreddit)
    if word:
      this=subreddit
      r =requests.get(f'https://www.reddit.com/r/{subreddit}/top/?t=month',headers=headers)
      soup= BeautifulSoup(r.text,"html.parser")
      subs =soup.find_all('div',{'class':'_1oQyIsiPHYt6nx7VOmd1sz'})
      for sub in subs:
        votes = sub.find("div", {"class":"_1rZYMD_4xY3gRcSS3p8ODO"})
        if votes:
          votes = votes.string
        title = sub.find("h3", {"class":"_eYtD2XCVieq6emjKBH3m"})
        if title:
          title = title.string
        link = sub.find("a", {"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})
        if link:
          link = link['href']
        if votes and title and link:
          reddits.append({'votes':int(votes), 'title':title, 'link':link, 'subreddit':subreddit})
      reddits.sort(key=lambda item: item['votes'], reverse=True)
      return render_template('read.html', reddits=reddits,this=this)
'''

@app.route("/add", methods=['post'])
def add():
  if request.method:
    new= request.form["new_subreddit"]
    if '/r/' in new:
      invalidate= 'write the name without /r/.'
      return render_template("add.html", invalidate=invalidate)
    else:
      if scrape_subreddit(new):
        subreddits.append(new)
        return home()
      else:
        invalidate= 'that subreddit does not exist.'
        return render_template("add.html", invalidate=invalidate)


  

app.run(host="0.0.0.0")
