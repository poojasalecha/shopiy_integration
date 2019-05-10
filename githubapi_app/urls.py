from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^packages$', views.get_top_packages, name='get_top_packages'),
	url(r'^search/repository/(?P<username>[\w\-]+)/v1.0$', views.get_repositories, name='get_repositories'),
	url(r'^count/(?P<username>[\w\-]+)/v1.0$', views.save_count_of_stars_forks, name='save_count_of_stars_forks'),
	url(r'^repos/(?P<owner>[\w\-_]+)/(?P<repo_name>[\w\-_]+)/v1.0$', views.save_package, name='save_package'),

]