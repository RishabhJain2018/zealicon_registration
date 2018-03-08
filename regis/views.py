from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ParticipantsForm, OnlineForm
from regis.models import ParticipantsDetail, ParticipantsOnline, SearchOnline
from profiles.models import UserDetail
from transaction.models import Transaction
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from django.template import Context, Template
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


def index(request):

	''' Views for Dashboard '''

	if request.user.is_authenticated():
		print(request.user.groups.all())
		if(request.user.groups.all()[0].name == 'others'):
			return HttpResponseRedirect('/index/search/')
		return render(request, 'index.html',{"others": False})
	else:
		return render(request,'login.html')
  

def online_regis(request):
	''' View for online registeration form '''
	if request.method == 'POST':
		# print(request.POST)
		form = OnlineForm(request.POST)
		if form.is_valid():
			temp = form.save()
			user = ParticipantsOnline.objects.get(pk=temp.id)
			zeal_id = 'ZO_'+str(temp.id)
			user.zeal_id_temp = zeal_id
			user.save()
			return render(request, "thank_you.html", {'zeal_id':zeal_id})
		else:
			return render(request, "online.html", {'form':form})
		return render(request, "online.html", {})
	else:
		return render(request, "online.html", {})


def administrator(request):
	
	''' Views For Login Into the Portal '''
	if not request.user.is_authenticated():
		if request.method=="POST":
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=auth.authenticate(username=username, password=password)
			if user==None:
				return render(request, 'login.html',{'error':1})
			if user.is_superuser:
				auth.login(request, user)
				return HttpResponseRedirect('admin/')
			elif user.is_staff:
				auth.login(request, user)
				return HttpResponseRedirect('index/')
			else:
				auth.login(request, user)
				if(request.user.groups.all()[0].name == 'others'):
					return HttpResponseRedirect('/index/search/')
				return render(request, 'index.html',{"others": False})
		elif request.method=="GET":
			return render(request, 'login.html')
	else:
		return HttpResponseRedirect("/index")



def participants_register(request):

	''' Views to register a Student '''
	if request.user.is_authenticated():
		form=ParticipantsForm()
		if request.method=="POST":
			form=ParticipantsForm(request.POST)
			if form.is_valid():
				data=form.cleaned_data
				if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
					form.cleaned_data['fee']=200
					fee=form.cleaned_data['fee']
				else:
					form.cleaned_data['fee']=200
					fee=form.cleaned_data['fee']

				return render(request, 'confirm.html', {'data':data,'fee':fee})
			else:
				return render(request, 'register.html', {'form':form})
		else:
			return render(request, 'register.html', {'form':form})
	else:
		return render(request, 'login.html')


def confirm(request):

	''' Views to confirm the registration '''
	if request.user.is_authenticated():
		if request.method=="POST":
			form=ParticipantsForm(request.POST)
			if form.is_valid():
				if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
					form.cleaned_data['fee']=200
				else:
					form.cleaned_data['fee']=200
				
				participant=form.save(commit=False)
				participant.fee=form.cleaned_data['fee']
				participant.created_by = User.objects.get(username=request.user)
				participant.save()
				participant_details=ParticipantsDetail.objects.get(pk=participant.id)
				participant_details.zeal_id = "Zeal"+str(participant.id)
				participant_details.save()

				if not 'print_id' in request.session or not request.session['print_id']:
					request.session['print_id']=["Zeal"+str(participant.id)]
					print request.session['print_id']

				else:
					print_list=request.session['print_id']
					print_list.append("Zeal"+str(participant.id))
					request.session['print_id']=print_list
					length=len(request.session['print_id'])

				# Logic to complete the transaction table.
				users = User.objects.exclude(username__contains='root')
				user_detail = []
				participant_created = []
				for user in users:
					participant_created.append(ParticipantsDetail.objects.filter(created_by=user))
				for i in participant_created:
					if len(i) == 0:
						pass
					else:
						jss_count = 0
						others_count = 0
						amount = 0
						for j in xrange(0,len(i)):
							if i[j].college == "JSS Academy of Technical Education [JSSATE], Noida":
								jss_count+=1
							else:
								others_count+=1
							created = i[j].created_by

						society = UserDetail.objects.get(user=created).college_society
						amount = jss_count*200 + others_count * 200

						try:
							transaction = Transaction.objects.get(username=created)
							transaction.username=created
							transaction.society=society
							transaction.jss_registration=jss_count
							transaction.other_registration=others_count
							transaction.amount=amount
							transaction.save()

						except ObjectDoesNotExist:
							Transaction.objects.create(username=created,society=society,
														jss_registration=jss_count,other_registration=others_count,
														amount=amount)

			return HttpResponseRedirect('print/')

		elif request.method=="GET":
			return render(request, 'confirm.html')
	else:
		return render(request, 'login.html')


def search(request):

	''' Views for online registration search'''
	if request.user.is_authenticated():
		if request.method=="POST":
			search=request.POST.get('search')
			print("IN HERE!")
			try:
				zeal_id_obj = ParticipantsOnline.objects.get(zeal_id_temp=search)
				#print(zeal_id_obj.name,"123")
				if ParticipantsDetail.objects.filter(email=zeal_id_obj.email):
					if(request.user.groups.all()[0].name == 'others'):
						 return render(request, 'search_online.html',{"error": "Email id or Mobile number already registered."})
					return render(request,'register_online.html',{"error": "Email id or Mobile number already registered."})
			except:
				if(request.user.groups.all()[0].name == 'others'):
					return render(request, 'search_online.html',{"error": "Sorry, you have not registered online."})
				return render(request, 'register_online.html', {'error': "Sorry, you have not registered online."})
			zeal_id = ParticipantsOnline.objects.filter(zeal_id_temp=search).values_list()
			if(request.user.groups.all()[0].name == 'others'):
				return render(request, 'search_online.html',{"zeal_id": zeal_id})
			print(zeal_id)
			return render(request,'register_online.html',{"zeal_id": zeal_id})
		return render(request, 'search_online.html')
	else:
		return render(request, 'login.html')


def online_register(request):

	''' Views for online registration '''
	if request.user.is_authenticated():
		if request.method=="POST":
			form=ParticipantsForm(request.POST)
			if form.is_valid():
				data=form.cleaned_data

				if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
					form.cleaned_data['fee']=200
					fee=form.cleaned_data['fee']
				else:
					form.cleaned_data['fee']=200
					fee=form.cleaned_data['fee']

				return render(request, 'confirm.html',{'data': data,'fee':fee})
		elif request.method=="GET":
			return render(request, 'search_online.html')
	else:
		return render(request, 'login.html')


def online_confirm(request):

	''' Views for online Conformation '''
	if request.user.is_authenticated():
		if request.method=="POST":
			form=ParticipantsForm(request.POST)
			if form.is_valid():
				if form.cleaned_data['college']=="JSS Academy of Technical Education [JSSATE], Noida":
					form.cleaned_data['fee']=200
				else:
					form.cleaned_data['fee']=200
				
				participant=form.save(commit=False)
				participant.fee=form.cleaned_data['fee']
				participant.created_by = User.objects.get(username=request.user)
				participant.save()
				participant_details=ParticipantsDetail.objects.get(pk=participant.id)
				participant_details.zeal_id="Zeal"+str(participant.id)
				participant_details.save()


				if not 'print_id' in request.session or not request.session['print_id']:
					request.session['print_id']=["Zeal"+str(participant.id)]
				else:
					print_list=request.session['print_id']
					print_list.append("Zeal"+str(participant.id))
					request.session['print_id']=print_list

			return HttpResponseRedirect('confirm/print/online')

		elif request.method=="GET":
			return render(request, 'confirm_online.html')
	else:
		return render(request, 'login.html')


def print_id(request):

	''' Views to print the ID'''
	if request.user.is_authenticated():
		try:
			print "inside"
			participant_obj = ParticipantsDetail.objects.filter(zeal_id__in=request.session['print_id'])
			# Loop to set the set flag value.
			for i in participant_obj:
				i.id_card_print=True
				i.save()
			return render(request,'icard.html',{'participant_obj':participant_obj})
		except:
			return render(request, "icard.html", {'error':1})
	else:
		return render(request, 'login.html')


def print_receipt(request):

	''' Views to print the Receipt '''
	if request.user.is_authenticated():
		try:
			participant_obj = ParticipantsDetail.objects.filter(zeal_id__in=request.session['print_id'])
			# Loop to set the flag value
			for i in participant_obj:
				i.receipt_print=True
				i.save()
			return render(request,'receipt.html',{'participant_obj':participant_obj})
		except:
			return render(request, "receipt.html", {'error':1})
	else:
		return render(request, 'login.html')


def reset_counter(request):
	if request.user.is_authenticated():
		if request.method == "GET":
			del request.session['print_id']
			return HttpResponseRedirect('/index')
	else:
		return render(request, 'login.html')



def print_offline(request):

	''' Views for print id number display '''
	if request.user.is_authenticated():
		if not 'print_id' in request.session or not request.session['print_id']:
			return render(request,'confirmed.html',{'error':1})
		else:
			zeal_id = request.session['print_id'][-1]
			length=len(request.session['print_id'])
			return render(request, 'confirmed.html', {'length':length, 'zeal_id': zeal_id})
	else:
		return render(request, 'login.html')


def print_online(request):

	''' Views for online print id number display'''
	if request.user.is_authenticated():
		if not 'print_id' in request.session or not request.session['print_id']:
			return render(request,'confirmed.html',{'error':1})
		else:
			zeal_id = request.session['print_id'][-1]
			length=len(request.session['print_id'])
			return render(request, 'confirmed.html', {'length':length, 'zeal_id': zeal_id})
	else:
		return render(request, 'login.html')


def custom(request):

	''' Views for custom Search '''
	if request.user.is_authenticated():
		if request.method=="POST":
			search=request.POST.get('search')
			try:
				zeal_id_obj=ParticipantsDetail.objects.get(email=search)
				print zeal_id_obj.__dict__
				if not 'print_id' in request.session or not request.session['print_id']:
					request.session['print_id']=[str(zeal_id_obj.zeal_id)]
					length=len(request.session['print_id'])
					return render(request, 'confirmed.html',{'length':length})
				else:
					print_list=request.session['print_id']
					print_list.append(str(zeal_id_obj.zeal_id))
					request.session['print_id']=print_list
					length=len(request.session['print_id'])

					return render(request, 'confirmed.html',{'length':length})

			except:
				return render(request,'custom_search.html')

		elif request.method=="GET":
			return render(request,'custom_search.html')
	else:
		return render(request, 'login.html')


def logout(request):
	if request.user.is_authenticated():
		auth.logout(request)
		return HttpResponseRedirect("/")
	else:
		return render(request, 'login.html')


def view_record(request):
	if request.user.is_authenticated():
		if request.user.groups.all()[0].name == 'quanta':
			transaction = Transaction.objects.all()
			amount = 0
			for i in transaction:
				amount+=float(i.amount)
			return render(request, 'view_record.html', {'transaction':transaction, 'amount':amount})
		else:
			return render(request, 'error_404.html')
	else:
		return render(request, 'login.html')


# Logic for Transaction table.
 
# users = User.objects.exclude(username__contains='root')
# participant_created = []
# user_detail = []
# for user in users:
#     participant_created.append(ParticipantsDetail.objects.filter(created_by=user))

# for i in participant_created:
#     jss_count = 0
#     others_count = 0
#     amount = 0
#     for j in xrange(0,len(i)):
#         if i[j].college == "JSS Academy of Technical Education [JSSATE], Noida":
#             jss_count+=1
#         else:
#             others_count+=1
#         created = i[j].created_by

#     society = UserDetail.objects.get(user=created).college_society
#     amount = jss_count*200 + others_count * 200

#     try:
#         transaction = Transaction.objects.get(username=created)
#         transaction.username=created
#         transaction.society=society
#         transaction.jss_registration=jss_count
#         transaction.other_registration=others_count
#         transaction.amount=amount
#         transaction.save()

#     except ObjectDoesNotExist:
#         Transaction.objects.create(username=created,society=society,
#                                     jss_registration=jss_count,other_registration=others_count,
#                                     amount=amount)
