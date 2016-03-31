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


def administrator(request):
    
    ''' Views For Administrator '''

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user.is_superuser:
            auth.login(request, user)
            return HttpResponseRedirect('admin/')
        elif user.is_staff:
            auth.login(request, user)
            return HttpResponseRedirect('index/')
    else:
        if not request.user.is_authenticated():
            return render(request, 'login.html',)
        else:
            if request.user.is_staff or request.user.is_superuser:
                return HttpResponseRedirect('/index/')


def index(request):
    ''' Views for Index Page '''
    return render(request, 'index.html')


def participants_register(request):
    ''' Views to register a Student '''

    form=ParticipantsForm()

    if request.method=="POST":
        form=ParticipantsForm(request.POST)
        print form
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
            participant_details=ParticipantsDetail.objects.get(pk=participant.id)
            participant_details.zeal_id = "Zeal"+str(participant.id)
            participant_details.save()
            print_list = request.session['print_id']
            print_list.append("Z16_"+str(participant.id))
            request.session['print_id'] = print_list
            return render(request, 'confirmed.html')

    return render(request, 'confirm.html')


def search(request):
    ''' Views for online registration'''

    if request.method=="POST":
        search=request.POST.get('search')
        try:
            zeal_id_obj = ParticipantsOnline.objects.get(zeal_id_temp=search)
            if ParticipantsDetail.objects.filter(email=zeal_id_obj.email):
                return render(request,'register_online.html',{"error": "Email id or Mobile number already registered."})
        except:
            return render(request, 'register_online.html', {'error': "Sorry, you have not registered online."})
        zeal_id = ParticipantsOnline.objects.filter(zeal_id_temp=search).values_list()
        return render(request,'register_online.html',{"zeal_id": zeal_id})
    return render(request, 'search_online.html', {})


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
            participant_details=ParticipantsDetail.objects.get(pk=participant.id)
            participant_details.zeal_id="Zeal"+str(participant.id)
            participant_details.save()
            return render(request, 'confirmed.html')

    return render(request, 'confirm.html')
