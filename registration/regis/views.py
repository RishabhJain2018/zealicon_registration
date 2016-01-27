from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ParticipantsForm
from django.views.generic import View
from regis.models import Participants_Details
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

def is_member(user, group_name):

	# Checks for the multiple users in the Group
	return Group.objects.get(name=group_name).user_set.filter(groups__name__in=['Quanta_user','Nibble_user']).exists()


class OrganizationView(View):
	''' Administartor Views '''

	template_name='admin.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username, password=password)
		for group in user.groups.all():
			if str(group) == 'Quanta_user' and is_member(user, group):
				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('register/')

			elif str(group) == 'Nibble_user' and is_member(user, group):
				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('admin/')

		else:
			return render(request, self.template_name)

	

class ParticipantsView(View):
	'''Views to Register a Student ''' 

	form_class= ParticipantsForm
	template_name = 'index.html'

	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name ,{form:'form'})

	def post(self, request):
		form=self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('fees/')
		return render(request, self.template_name,{'form':form})


class FeesView(View):
	''' Fee Submission views '''

	template_name='fees.html'

	def get(self, request):
		return render(request, self.template_name)

		