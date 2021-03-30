from django.shortcuts import render
from sign.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.



def index(request):
    return render(request, 'temp/index.html')

@login_required ## it is for the route security , to view content he should login first 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False
    if request.method == 'POST':
    
        user_form = UserForm(data=request.POST)
        user_info = UserProfileForm(data=request.POST)

        if user_form.is_valid() and user_info.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_info.save(commit=False)
            profile.user = user

            if 'profile_img' in request.FILES:
                profile.profile_img = request.FILES['profile_img']
                print(profile.profile_img)
            profile.save()
            registered = True
        else:
            print(user_form.errors, user_info.errors)

    else:
        user_form = UserForm()
        user_info = UserProfileForm()
    return render(request, 'temp/register.html', {'user_form':user_form, 'profiles_form':user_info, 'registered':registered})
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE!')
    
        else:
            print('Someone tried to login and faild')
            print('Username  : {} , password: {}'.format(username,password))
            return HttpResponse('invalid credentials!')
    
    else:
        return render(request, 'temp/login.html', {})