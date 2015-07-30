from django.conf.urls import include, url
urlpatterns = [
    url(r'^$', 'userProfile.views.users'),
    url(r'^follow/(?P<user_id>\d+)/$', 'userProfile.views.followUser'),
    ]
