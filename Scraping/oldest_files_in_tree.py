import os, heapq

def oldest_files_in_tree(rootfolder, count=1):
    return heapq.nsmallest(count,
        (os.path.join(dirname, filename)
        for dirname, dirnames, filenames in os.walk(rootfolder)
        for filename in filenames),
        key=lambda fn: os.stat(fn).st_mtime)


if Article_Base.objects.all() :
             all_articles = Article_Base.objects.all().order_by('date')
             m = len(all_articles)
             if m > 5 :
                  if n > m :
                       oldest_articles = all_articles[:m] #Makes a list of the n oldest txt files; with m = number of old articles
                  else :
                       oldest_articles = all_articles[:n] #Makes a list of the n oldest txt files; with n = number of new articles

                  for old_article in oldest_articles : #Remove n oldest files
                       old_article.delete()
