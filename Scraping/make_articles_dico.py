#With module : newspaper

import newspaper

#Creates a dictionnary with articles' name and url

def make_articles_dico (paper_name, papers_dico) : 
    
    paper=newspaper.build(papers_dico[paper_name], memoize_articles=False)    #Builds a news source.
    articles_dico ={}
    
    for article in paper.articles :
        title = article.title
        if title != "404 Page Not Found" : #If title not found, just forget it
            for character in title :
                title=title.replace("  ", "")
                title=title.replace("\n", "")
                title=title.replace("\t", "")
                title=title.replace("\r", "")
            if title not in ["", " "] : #If title == bullshit, just forget it   
                if len(title) > 10: #You don't want a lengthy name for your file
                    title=title[:10]
                articles_dico[title] = article.url
            
    return(articles_dico)
