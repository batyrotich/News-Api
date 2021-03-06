from app import app
import urllib, json
from app.models.news import Source, Article
import requests


#Getting API key 
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

# Getting the articles base url
article_base_url = app.config['ARTICLE_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(api_key)
    res = requests.get(get_source_url)
    data = res.json().get('sources')
    return process_sources(data)
def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        county = source_item.get('country')
        
        if url:
            sources_object = Source(id, name, description, url, category, language, county)
            sources_results.append(sources_object)
        
    return sources_results


def get_articles(source_id):
    get_articles_url = base_url_article.format(source_id, api_key)
    res = requests.get(get_articles_url)
    articles_data = res.json().get('articles')

    return process_articles(articles_data)

def process_articles(articles_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    articles = []
    if articles_list:
        for article in articles_list:
            id = article.get('id')
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')
            content = article.get('content') 
            articles.append(article)
        return articles

        
