from flask import Flask,render_template,redirect,url_for
from . import main
from ..request import get_news, get_source,news_search
from ..models import Source

#Views
@main.route('/')
def index():
  '''
  View function to display the index page and its data
  '''
  #Getting news sources
  # sources = get_news('sources')

  source = get_news()
  title = 'Home - Welcome to the best News website online'

  return render_template('index.html', title = title, sources = source)

@main.route('/sources/<name>')
def source(name):
  print(name)
  specific_sources = get_source(name)
  title = f'{name}'

  return render_template('news_source.html', specific_sources = specific_sources)

@main.route('/search/<news_name>')
def search(news_name):
  '''
  View function to display the search results
  '''
  news_name_list = news_name.split(" ")
  news_name_format = "+".join(news_name_list)
  searched_news = news_search(news_name_format)
  title = f'search results for {news_name}'
  return render_template('search.html',news = searched_news)