import unittest
from app.models import Source

class NewsTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the news class
  '''
  def setUp(self):
    '''
    A setup function that will run before any test
    '''
    self.new_news = News('ABC News', 'Your trusted source for breaking news', 'https://abcnews.go.com',
    'general', 'en','country')

  def test_init(self):
    '''
    Tests whether the news object is instantiated correctly
    '''
    self.assertTrue(instance(self.new_news, Source))

