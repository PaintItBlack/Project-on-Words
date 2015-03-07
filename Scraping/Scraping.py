import os #used for path making
import io #used for encoding option when writing
from make_articles_dico import make_articles_dico
from scrape_article_content import scrape_article_content

papers_dico = {"huffingtonpost" : 'http://huffingtonpost.com'}

def scraping(papers_dico):

     #make_articles_dico=fct : (paper_name, papers_dico) as (str,dict) -> dict
     #scrape_article_content = fct : (article_url) as str -> str

#Makes a file for each article from each newspaper
     for paper_name in list(papers_dico) :
        articles_dico=make_articles_dico(paper_name, papers_dico) #Returns a dictionary {article_name : article_url}
        print(articles_dico)
        for article_name in list(articles_dico) :
            file_name = "%s\%s.txt" %(paper_name, article_name)
            content=scrape_article_content(articles_dico[article_name]) #Returns the body of the article
            
            if not os.path.exists(paper_name): #Checks if a folder named after the newspaper exists
                os.makedirs(paper_name)
                print("%s in the making" %papername)
        
            output = io.open(file_name,"w", encoding="utf8")
            output.write(content)
            output.close()
