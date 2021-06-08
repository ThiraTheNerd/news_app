class Source:
  '''
  Source class to define Movie objects
  '''
  def __init__(self,source,author,title,description,url,urlToImage,publishedAt):
    self.source = source
    self.author= author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt

class Article:
  '''
  Article class to define an artivle object
  '''

  def __init__(self,source,author,title,description,url, urlToImage,publishedAt):
    self.source = source
    self.author = author
    self.title = title
    self.description = description
    self.urlToImage = urlToImage
    self.url = url
    self.publishedAt = publishedAt


