from django.shortcuts import render
from basic_app import forms, models
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import (ListView, TemplateView,
                                  DetailView)

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False
    if request.method=='POST':
        userForm = forms.UserForm(data=request.POST)
        if userForm.is_valid():
            user = userForm.save()
            #user.password(user.password)
            #user.save()
            # Registration Successful!
            registered = True

    else:
        userForm = forms.UserForm()

    return render(request, 'basic_app/register.html', {'userForm':userForm,
                                                        'registered': registered})



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Django's built-in authentication function:
        user = authenticate(username=email, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

class NoticeListView(ListView):
    model = models.Notice
    context_object_name = 'notices'
    template_name = 'basic_app/viewnotice.html'

class NoticeDetailView(DetailView):
    model = models.Notice
    context_object_name = 'notice_detail'
    template_name = 'basic_app/notice_detail.html'
