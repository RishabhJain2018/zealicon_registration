from .models import UserDetail
from .forms import UserForm, UserDetailForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def profile(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			username = request.user
			user = get_object_or_404(User, pk=username.id)
			user_form = UserForm(request.POST, instance=user)
			detail, create = UserDetail.objects.get_or_create(user=user)
			detail_form = UserDetailForm(request.POST, instance=detail)
			if user_form.is_valid() and detail_form.is_valid():
				user_form.save()
				detail_form.save()
				return HttpResponseRedirect('/index')
			else:
				return render(request, 'profile.html')
		else:
			return render(request, 'profile.html')
	else:
		return HttpResponseRedirect("/")
