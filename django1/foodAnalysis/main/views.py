# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import never_cache

from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm


username = ''


@never_cache
@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')


@never_cache
@login_required(login_url="/login")
def special(request):
    return HttpResponse("You are logged in !")


@never_cache
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'login.html', {'login_form': form})



