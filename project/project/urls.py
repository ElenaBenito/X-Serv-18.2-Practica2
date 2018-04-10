from django.conf.urls import include, url
from django.contrib import admin
from acorta import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', views.list),
	url(r'^(\d+)$', views.redirect),
	url(r'^admin/', include(admin.site.urls)),
	
]

