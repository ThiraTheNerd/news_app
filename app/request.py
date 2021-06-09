import urllib.request, json
from .models import Article

#Getting the API_KEY
api_key = None

#Getting the news base url
base_url = None

#Getting the categories base url
categorie_url = None
#Getting the top_headlines url
topheadlines_url = None
#Getting the sources url
source_url = None
#Getting the search news url
search_news_url = None

def configure_request(app):
  global api_key, base_url, categories_url, topheadlines_url, source_url,search_news_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config["NEWS_API_BASE_URL"]
  categories_url = app.config['CATEGORIES_BASE_URL']
  topheadlines_url = app.config['TOP_HEADLINES_URL']
  source_url = app.config['SOURCE_URL']
  search_news_url = app.config['SEARCH_NEWS_URL']


def get_news():
  '''
  Function that gets the json response to our URL
  '''
  get_news_url = topheadlines_url.format(api_key)

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['articles']:
      news_results_list = get_news_response['articles']
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
    source = news_source.get('source')
    author = news_source.get('author')
    title = news_source.get('title')
    description = news_source.get('description')
    url = news_source.get('url')
    urlToImage= news_source.get('urlToImage')
    publishedAt = news_source.get('publishedAt')

    if source["id"] & urlToImage:
      news_source_object = Article(source, author,title, description, url, urlToImage, publishedAt)
      news_sources.append(news_source_object)
  
  return news_sources

def get_source(name):
  get_source_url = source_url.format(name,api_key)

  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    get_source_response = json.loads(get_source_data)

    source_results = []
    if get_source_response['articles']:
      source_results_list = get_source_response['articles']
      
      source_results = process_sources(source_results_list)

  return source_results

def process_sources(sources_list):
  sources_results = []
  for source_item in sources_list:
    source = source_item.get('source')
    author = source_item.get('author')
    title = source_item.get('title')
    description = source_item.get('description')
    url = source_item.get('url')
    urlToImage = source_item.get('urlToImage')
    publishedAt= source_item.get('publishedAt')

    if source["id"]:
      source_object = Article(source, author,title, description, url, urlToImage, publishedAt)
      print(source_object)
      sources_results.append(source_object)

  return sources_results

def news_search(news_name):
  news_url= search_news_url.format(news_name,api_key)

  with urllib.request.urlopen(news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    searched_news = []

    if get_news_response["articles"]:
      searched_news_list = get_news_response['articles']
      searched_news = process_results(searched_news_list)
  return searched_news

def process_results(news_list):
  '''
  Function  that processes the news result and transform them to a list of Objects

  Args:
    news_list: A list of dictionaries that contain news details

  Returns :
    news_results: A list of news objects
  '''
  articles_results = []

  for article_item in news_list:
    source = article_item.get('source')
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    url = article_item.get('url')
    urlToImage = article_item.get('urlToImage')
    publishedAt= article_item.get('publishedAt')

    if urlToImage:
      articles_object = Article(source,author,title,description,url,urlToImage,publishedAt)
      articles_results.append(articles_object)

  return articles_results

