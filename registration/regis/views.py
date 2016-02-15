from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ParticipantsForm
from django.views.generic import View
from regis.models import Participants_Details, Participants_Online
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from django.template import Context, Template
from django.shortcuts import get_object_or_404


def is_member(user, group_name):
	
	''' Checks for the multiple users in the Group'''

	return Group.objects.get(name=group_name).user_set.filter(groups__name__in=['Quanta_user','Nibble_user']).exists()
		

def administrator(request):
	''' Views For Administrator '''

	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username, password=password)
		for group in user.groups.all():
			if str(group) == 'Quanta_user' and is_member(user, group):
				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('index/')

			elif str(group) == 'Nibble_user' and is_member(user, group):
				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('admin/')
	
	return render(request, 'base.html')


def index(request):
	''' Views for Index Page '''

	return render(request, 'index.html')


def participants_register(request):
	''' Views to register a Student '''

	form=ParticipantsForm()

	if request.method=="POST":
		form=ParticipantsForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			form.save()
			return render(request, 'confirm_registration.html', {'data':data})
	
	else:
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def confirm(request):
	''' Views for the conformation '''

	return render(request, 'confirm.html')


def online(request):
	''' Views for online registration'''

	return render(request, 'online.html')


def online_search(request):
	if request.method=="POST":
		search_text = request.POST['search_text']
	else:
		search_text=''

	zealids = Participants_Online.objects.filter(zealid__contains=search_text)

	return render(request, 'ajax_search.html', {'zealids': zealids })






# class OrganizationView(View):
# 	''' Administartor Views '''

# 	template_name='admin.html'

# 	def get(self, request):
# 		return render(request, self.template_name)

# 	def post(self, request):
# 		username=request.POST.get('username')
# 		password=request.POST.get('password')
# 		user=auth.authenticate(username=username, password=password)
# 		for group in user.groups.all():
# 			if str(group) == 'Quanta_user' and is_member(user, group):
# 				if user is not None and user.is_active:
# 					auth.login(request, user)
# 					return HttpResponseRedirect('index/')

# 			elif str(group) == 'Nibble_user' and is_member(user, group):
# 				if user is not None and user.is_active:
# 					auth.login(request, user)
# 					return HttpResponseRedirect('admin/')

# 		else:
# 			return render(request, self.template_name)

# def index(request):
# 	return render(request, 'index.html')


# class ParticipantsView(View):
# 	'''Views to Register a Student ''' 

# 	form_class= ParticipantsForm
# 	template_name = 'register.html'

# 	def get(self, request):
# 		form = self.form_class()
# 		return render(request, self.template_name ,{form:'form'})

# 	def post(self, request):
# 		form=self.form_class(request.POST)
# 		if form.is_valid():
# 			data=form.cleaned_data
# 			form.save()
# 			return render(request, 'confirm_registration.html' ,{'data':data})
# 		else:
# 			return render(request, self.template_name, {'form':form})
