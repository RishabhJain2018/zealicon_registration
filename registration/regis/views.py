from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ParticipantsForm
from django.views.generic import View
from regis.models import Participants_Details
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

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
			return HttpResponseRedirect('/fees')
		return render(request, self.template_name,{'form':form})


class FeesView(View):
	''' Fee Submission views '''

	template_name='fees.html'

	def get(self, request):
		return render(request, self.template_name)

def is_member(user, group_name):
	return Group.objects.get(name=group_name).user_set.filter(username='quanta_user').exists()

class OrganizationView(View):
	''' Administartor Views '''

	template_name='admin.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		print "first if"
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username, password=password)
		if is_member(user, 'Quanta_user'):
			if user is not None:
				print "Second if"
				if user.is_active:
					print "Third if"
					auth.login(request,user)
					return HttpResponseRedirect('/home')
				else:
					return render(request, self.template_name)
			else:
				return render(request, self.template_name)
		else:
			return render(request, self.template_name)
		# else:
			# return render(request, self.template_name)



