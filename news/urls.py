
from django.conf.urls import include, url

urlpatterns = [
#smotrit adress, i potom napravlyaet na tu funktsiyu
    url(r'^', 'news.views.news'),


]