from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.views.generic import View
from regis.models import Register

class RegisterView(View):
	'''Views to Register a Student ''' 
	form_class= RegisterForm
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