_author_ = 'root@timofey-PC'

from django.forms import ModelForm
from comments.models import Comments

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ['comments_text']