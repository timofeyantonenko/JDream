_author_ = 'root@timofey-PC'

from django.forms import ModelForm
from talent.models import Talent

class TalentForm(ModelForm):
	class Meta:
		model = Talent
		fields = ['talent_title', 'talent_text']