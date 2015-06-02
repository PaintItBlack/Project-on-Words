urlpatterns = patterns('Tree_Show.views',
    url(r'^$', 'Tree_Appear'),
    url(r'^(?P<name>[-\w\d]+)$', 'Paper_Appear'), #/paper
    url(r'^(?P<paper>[-\w\d]+)/(?P<slug>[-\w\d]+),(?P<pk>\d+)/$', 'Article_Appear') #/paper/slug,id/
                       )
