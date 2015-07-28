from django.shortcuts import render
#import dlya responsa
from django.http.response import HttpResponse
#shtob' ispolzovat render_to_response
from django.shortcuts import render_to_response
#importiruem modeli dlya zaprosov k BD
from news.models import News

# Create your views here.
#vivodit vse novosti
def news(request):
	#beret is news vse danniye
	return render_to_response('news.html',{'news': News.objects.all()})