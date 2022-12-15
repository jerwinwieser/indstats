from django import forms
from core.models import Application

class ApplicationForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = ['name', 'submitdate', 'comments']