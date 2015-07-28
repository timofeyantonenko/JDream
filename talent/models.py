# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Talent(models.Model):
	# klass Meta vklyuchaet dopolnitel'nye svoystva dlya nashey budushchey tablitsy
	class Meta():
		db_table = "talent"
	# kolonka otvechayushchaya za zagolovok stat'i

	talent_title = models.CharField(max_length=200)
	# kolonka otvechayushchaya za tekst stat'i, mozhet bit' pustim
	talent_text = models.TextField(blank=True, null=True)
	# kolonka otvechayushchaya za khraneniya daty i vremya sozdaniya stat'i
	talent_date = models.DateTimeField(default = timezone.now)
	# kolonka otvechayushchaya za khraneniya ochkov prodvizheniya stat'i, 0 po umolchanitu
	talent_likes = models.IntegerField(default=0)
	#kto hozyain formi
	talent_from = models.ForeignKey(User, default=1)



