
from django.conf.urls import include, url

urlpatterns = [
#smotrit adress, i potom napravlyaet na tu funktsiyu

    url(r'^login/$', 'loginsys.views.login'),
    url(r'^logout/$', 'loginsys.views.logout'),
    url(r'^register/$', 'loginsys.views.register'),

]
