#lol
def Article_Appear(request, paper, slug, pk): #lowest level tree
        article = get_object_or_404(Article_Base, pk = pk) #get the article thanks to the unique id=pk from the url request
        return render(request, "Article_Show.html", {"dicojson" : article.dico, "url" : article.url}) #Calls the template Article_Show.html ; gives it a dictionary and a url
