import urllib.request, json
from .models import Source,Article

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

def configure_request(app):
  global api_key, base_url, categories_url, topheadlines_url, source_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config["NEWS_API_BASE_URL"]
  categories_url = app.config['CATEGORIES_BASE_URL']
  topheadlines_url = app.config['TOP_HEADLINES_URL']
  source_url = app.config['SOURCE_URL']


def get_news():
  '''
  Function that gets the json response to our URL
  '''
  print(topheadlines_url)
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
    description = news_source.get('description')
    url = news_source.get('url')
    urlToImage= news_source.get('urlToImage')
    publishedAt = news_source.get('publishedAt')

    news_source_object = Source(source, author, description, url, urlToImage, publishedAt)
    news_sources.append(news_source_object)
  
  return news_sources

def get_source(id):
  get_source_url = source_url.format(id,api_key)

  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read
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
    urlToImage = source_item.get('urlToImage')
    url = source_item.get('url')
    author = source_item.get('author')
    description = source_item.get('description')
    title = source_item.get('title')
    publishedAt= source_item.get('publishedAt')

    source_object = Source(source, author, description, url, urlToImage, publishedAt)
    sources_results.append(source_object)

  return sources_results


# def get_articles(category):
#   '''
#   Function that gets the json response to our url
#   '''
#   get_articles_url = categories_url.format(category,api_key)
#   # print(get_articles_url)
#   # print(api_key)

#   with urllib.request.urlopen(get_articles_url) as url:
#     get_articles_data = url.read()
#     get_articles_response = json.loads(get_articles_data)

#     article_results = []

#     if get_articles_response['articles']:
#       articles_results_list = get_articles_response['articles']
#       print(articles_results_list)

#       articles_results = process_results(articles_results_list)


#   return articles_results

# def process_results(articles_list):
#   '''
#   Function  that processes the news result and transform them to a list of Objects

#   Args:
#     news_list: A list of dictionaries that contain news details

#   Returns :
#     news_results: A list of news objects
#   '''
#   articles_results = []

#   for article_item in articles_list:
#     source = article_item.get('source')
#     urlToImage = article_item.get('urlToImage')
#     url = article_item.get('url')
#     author = article_item.get('author')
#     description = article_item.get('description')
#     title = article_item.get('title')
#     publishedAt= article_item.get('publishedAt')

#     if urlToImage:
#       articles_object = Article(source,author,title,description,urlToImage, url,publishedAt)
#       articles_results.append(articles_object)

#   return articles_results

