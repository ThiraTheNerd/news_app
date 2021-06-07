from flask import Flask,render_template
from app import app
from .request import get_news

#Views
@app.route('/')
def index():
  '''
  View function to display the index page and its data
  '''
  #Getting news sources
  sources = get_news('sources')
  print(sources)
  title = 'Home - Welcome to the best News website online'

  return render_template('index.html', title = title, news_source = sources)