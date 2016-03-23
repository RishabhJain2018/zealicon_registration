from django import forms
from .models import ParticipantsDetail

class ParticipantsForm(forms.ModelForm):
	class Meta:
		model = ParticipantsDetail
		fields= ['name','email','course','branch','contact','college','year']

