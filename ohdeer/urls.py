from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.views.generic import TemplateView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^', include('deermap.urls', namespace="deermap")),
    #url(r'^admin/', include(admin.site.urls)),
	#url(r'^index/', TemplateView.as_view(template_name='index.html')),
)

#urlpatterns += staticfiles_urlpatterns()
