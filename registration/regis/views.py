from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ParticipantsForm
from django.views.generic import View
from regis.models import ParticipantsDetail, ParticipantsOnline, SearchOnline
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from django.template import Context, Template
from django.shortcuts import get_object_or_404


def is_member(user, group_name):
	
	''' Checks for the multiple users in the Group '''

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
				else:
					return render(request, "base.html", {"error":1})

			elif str(group) == 'Nibble_user' and is_member(user, group):
				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('admin/')

	return render(request, 'login.html')


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
			if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
				form.cleaned_data['fee']=150
				fee=form.cleaned_data['fee']
			else:
				form.cleaned_data['fee']=200
				fee=form.cleaned_data['fee']

			return render(request, 'confirm.html', {'data':data,'fee':fee})
	else:
		return render(request, 'register.html', {'form':form})


def confirm(request):
	''' Views for the conformation '''

	if request.method=="POST":
		form=ParticipantsForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
				form.cleaned_data['fee']=150
			else:
				form.cleaned_data['fee']=200
			
			participant=form.save(commit=False)
			participant.fee=form.cleaned_data['fee']
			participant.save()
			return render(request, 'confirmed.html')

	return render(request, 'confirm.html')


def online_display(request):
	''' Views for online registration'''

	if request.method=="POST":
		search=request.POST.get('search')
		zeal_id_temp=ParticipantsOnline.objects.filter(zeal_id_temp__contains=search).values_list()
		return render(request,'register_online.html',{"zeal_id_temp": zeal_id_temp})

	return render(request, 'search_online.html')

def online_register(request):
	if request.method=="POST":
		form=ParticipantsForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
				form.cleaned_data['fee']=150
				fee=form.cleaned_data['fee']
			else:
				form.cleaned_data['fee']=200
				fee=form.cleaned_data['fee']
			return render(request, 'confirm.html',{'data': data,'fee':fee})
	else:
		return render(request, 'search_online.html')


def online_confirm(request):

	if request.method=="POST":
		form=ParticipantsForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
				form.cleaned_data['fee']=150
			else:
				form.cleaned_data['fee']=200
			
			participant=form.save(commit=False)
			participant.fee=form.cleaned_data['fee']
			participant.save()
			return render(request, 'confirmed.html')

	return render(request, 'confirm.html')
