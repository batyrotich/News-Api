from app import app
import urllib, json
from app.models.news import Source, Article


#Getting API key 
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

# Getting the articles base url
article_base_url = app.config['ARTICLE_API_BASE_URL']
