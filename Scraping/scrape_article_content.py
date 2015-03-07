#With newspaper module

import newspaper

#Scrapes content of an article

def scrape_article_content(article_url) :
    article=newspaper.Article(url=article_url)
    article.download()
    article.parse()
    return(article.text)
