from app import app
import urllib.request, json
from .models import news

News = news.News

#Getting the API_KEY
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(source):
  '''
  Function that gets the json response to our URL
  '''
  get_news_url = base_url.format(source,api_key)

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['sources']:
      news_results_list = get_news_response['sources']
      news_results = process_results(news_results_list)

  return news_results

def process_results(news_list):
  '''
  Function that processes the news results and transform them into a list of objects
  Args:
    news_result a list of news objects

  returns: 
    news_results: a list of movie objects
  '''
  news_sources = []
  for news_source in news_list:
    id = news_source.get('id')
    name = news_source.get('name')
    description = news_source.get('description')
    url = news_source.get('url')
    category = news_source.get('general')
    language = news_source.get('language')
    country = news_source.get('country')

    news_source_object = News(id,name,description,url,category,language,country)
    news_sources.append(news_source_object)
  
  return news_sources



