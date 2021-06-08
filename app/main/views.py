from flask import Flask,render_template,redirect,url_for
from . import main
from ..request import get_news, get_source
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

@main.route('/sources/<source_id>')
def source(source_id):
  print(source_id)
  specific_sources = get_source({"sources": str(source_id)})
  title = f'{specific_source.id}'

  return render_template('news_source.html', specific_sources = specific_sources)