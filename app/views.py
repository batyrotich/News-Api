from app import app
from flask import render_template


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Top News  Highlight Website Online'
    return render_template('index.html', title = title)



@app.route('/articles/<id>')
def news(id):
    article = get_articles(id)
    print(article)
    return render_template('articles.html',article = article)

