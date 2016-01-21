from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.views.generic import View
from regis.models import Register

# Create your views here.
class RegisterView(View):
	form_class= RegisterForm
	template_name = 'index.html'
	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name ,{form:'form'})

	def post(self, request):
		form=self.form_class()
		try:
			name=request.POST.get('name')
			email=request.POST.get('email')
			course=request.POST.get('course')
			branch=request.POST.get('branch')
			contact=request.POST.get('contact')
			college=request.POST.get('college')
			college_name=request.POST.get('college_name')
			year=request.POST.get('year')
			Register.objects.create(name=name,email=email,course=course,branch=branch,contact=contact,college=college,college_name=college_name,year=year)
			return HttpResponseRedirect('/fees')
		except :
			return render(request, self.template_name,{'form':form})

		return render(request, self.template_name,{'form':form})

class FeesView(View):
	template_name='fees.html'
	def get(self, request):
		return render(request, self.template_name)