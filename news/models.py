from django.db import models

# Create your models here.
class News(models.Model):
	#klass Meta vklyuchaet dopolnitel'nye svoystva dlya nashey budushchey tablitsy
	class Meta():
		db_table = "news"
	#kolonka otvechayushchaya za zagolovok nowosti
	news_title = models.CharField(max_length = 200)
#kolonka otvechayushchaya za tekst stat'i, mozhet bit' pustim
	news_text = models.TextField(blank = True, null = True)
#kolonka otvechayushchaya za khraneniya daty i vremya sozdaniya nowosti
	news_date = models.DateTimeField()
