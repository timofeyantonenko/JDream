from django.contrib import admin
from news.models import News

# Register your models here.
#sozdaem class, v kotorom ukazhem dopustimie voampzhnosti admina 


#zaregestriruem na sayte novost'
admin.site.register(News)
