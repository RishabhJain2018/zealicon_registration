from django import forms
from .models import ParticipantsDetail, ParticipantsOnline

class ParticipantsForm(forms.ModelForm):
	class Meta:
		model = ParticipantsDetail
		fields= ['name','email','course','branch','contact','college','year']

class OnlineForm(forms.ModelForm):
	class Meta:
		model = ParticipantsOnline
		fields = ['name', 'email', 'course', 'branch', 'contact', 'college', 'year']
