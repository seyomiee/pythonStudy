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
