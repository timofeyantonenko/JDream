from django.contrib import admin
from talent.models import Talent
from comments.models import Comments

# Register your models here.
#sozdaem class, s pomoshyu kotorogo mozhno dobavlyat' i redactirovat' kommenti
class TalentInline(admin.StackedInline):
	#klass rabotaet s kommentami
	model = Comments
	#kol-vo kommentov po umolchaniyu otobr dlya vvoda
	extra = 2

	fields = ['comments_text']


#sozdaem class, v kotorom ukazhem dopustimie voampzhnosti admina 
class TalentAdmin(admin.ModelAdmin):
	#ukazivaem otobrazhemie polya
	fields = ['talent_title', 'talent_text', 'talent_date']
	inlines = [TalentInline]
	list_filter = ['talent_date']


#zaregestriruem na sayte talant'
admin.site.register(Talent, TalentAdmin)
