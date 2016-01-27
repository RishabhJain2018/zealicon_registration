from django import forms
from .models import Participants_Details

class ParticipantsForm(forms.ModelForm):
	class Meta:
		model = Participants_Details
		fields= '__all__'

