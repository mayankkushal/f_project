from django import forms

from .models import BasicModel

class BasicForm(forms.ModelForm):
	class Meta:
		model = BasicModel
		fields = ('__all__')