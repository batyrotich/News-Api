import unittest
from models.news import Source, Article

# Test class for the sources class
class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")

    def test_isSourceInstance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'abc-news')
        self.assertEquals(self.new_source.name,'ABC News')
        self.assertEquals(self.new_source.description,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEquals(self.new_source.url,'https://abcnews.go.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.language,'en')
        self.assertEquals(self.new_source.country,'us')
        

#test class for the articles
class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_article=Article("null", "Gizmodo.com", "John Biggs", "Crypto Traders Cut Out the Middleman, Simply Rob Victim", "https://gizmodo.com/crypto-traders-cut-out-the-middleman-simply-rob-victim-1845011301", "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/li0fkkejdmaugm8v1fkw.jpg", "2020-09-10T14:28:00Z", "Two alleged crypto traders in Singapore apparently came up with a fool-proof plan: rather than convert a customers 365,000 Singapore dollars to bitcoin, they would simply rob the victim when he came … [+1735 chars]")
    
    def test_isArticleInstance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'null')
        self.assertEquals(self.new_article.name,'Gizmodo.com')
        self.assertEquals(self.new_article.author,'John Biggs')
        self.assertEquals(self.new_article.title, 'Crypto Traders Cut Out the Middleman, Simply Rob Victim')
        self.assertEquals(self.new_article.description,'Two alleged crypto traders in Singapore apparently came up with a fool-proof plan: rather than convert a customer’s 365,000 Singapore dollars to bitcoin, they would simply rob the victim when he came in to do the trade.Read more...')
        self.assertEquals(self.new_article.url,'https://gizmodo.com/crypto-traders-cut-out-the-middleman-simply-rob-victim-1845011301')
        self.assertEquals(self.new_article.urlToImage, 'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/li0fkkejdmaugm8v1fkw.jpg')
        self.assertEquals(self.new_article.publishedAt, '2020-09-10T14:28:00Z')
        self.assertEquals(self.new_article.content, 'Two alleged crypto traders in Singapore apparently came up with a fool-proof plan: rather than convert a customers 365,000 Singapore dollars to bitcoin, they would simply rob the victim when he came … [+1735 chars]')

if __name__ == '__main__':
    unittest.main()


