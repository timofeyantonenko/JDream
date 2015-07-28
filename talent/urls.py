
from django.conf.urls import include, url

urlpatterns = [
#smotrit adress, i potom napravlyaet na tu funktsiyu
    url(r'^1/', 'talent.views.basic_one'),
    url(r'^2/', 'talent.views.template_two'),
    url(r'^3/', 'talent.views.template_three_simple'),
    # $ - okonchanie stroki v reg virazhenii
    url(r'^talents/all/$', 'talent.views.talents'),
    #(?P<imya peremennoy>\d+), d+ - dolzhno biy' cifroy
    url(r'^talents/get/(?P<talent_id>\d+)/page/(?P<page_number>\d+)/', 'talent.views.talent'),
    url(r'^talents/get/(?P<talent_id>\d+)/$', 'talent.views.talent'),
    url(r'^talents/addlike/(?P<talent_id>\d+)/$', 'talent.views.addlike'),
    url(r'^talents/addcomment/(?P<talent_id>\d+)/$', 'talent.views.addcomment'),
    url(r'^page/(\d+)/$', 'talent.views.talents'),
    url(r'^talents/addtalent/$', 'talent.views.addtalent'),
    url(r'^', 'talent.views.talents'),



]
