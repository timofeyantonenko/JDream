# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#importiruem modeli dlya zaprosov k BD
from talent.models import Talent


# Create your models here.
# klass kommenov
class Comments(models.Model):
	class Meta():
		db_table = "comments"

	# kolonka otvechayuchaya za tekst kommenta

	comments_text = models.TextField(verbose_name="Текст комментария")
	# kolonka otvechayuchaya za svyaz' kommenta i talanta
	comments_talent = models.ForeignKey(Talent)
	# kolonka otvechayushchaya za khraneniya ochkov prodvizheniya kommenta, 0 po umolchanitu
	comments_likes = models.IntegerField(default=0)
	# kolonka otvechayushchaya za khraneniya daty i vremya sozdaniya stat'i
	comments_date = models.DateTimeField(default = timezone.now)
	# kto ostavil komment
	comments_from = models.ForeignKey(User, default=1)
