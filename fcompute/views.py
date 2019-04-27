from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout, login, authenticate
from . forms import LoginForm


def home(request):
	return render(request, 'home.html')


@require_http_methods(['GET', 'POST'])
def main_login(request):
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('players')
			else:
				return redirect('login')

	kwargs = locals()
	return render(request, "login.html", kwargs)


def main_logout(request):
	logout(request)
	return render(request, "logout.html")
