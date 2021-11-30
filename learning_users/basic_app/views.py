from django.shortcuts import render
from basic_app.forms import JoyanUserForm, JoeUserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib. auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')
# This is a decorator for chekcin log in on
@login_required
def joe_user_logout (request):
    logout(request)
    # see in urls.py at project level that name given for the url for index is joyan_index
    return HttpResponseRedirect(reverse('joyan_index'))


def register(request):
    registered = False
    if request.method == 'POST':
        inst_of_user_form = JoyanUserForm(data=request.POST)
        inst_of_profile_form = JoeUserProfileInfoForm(data=request.POST)

        if inst_of_user_form.is_valid() and inst_of_profile_form.is_valid():
            user_joe = inst_of_user_form.save()
            user_joe.set_password (user_joe.password)
            user_joe.save()

            profile_jj = inst_of_profile_form.save(commit = False)
            profile_jj.user = user_joe
            # Commented as Pilllow is not geing isntalled.
            if 'joy_profile_pic' in request.FILES:
                profile_jj.joyan_profile_pic= request.FILES['joy_profile_pic']

            profile_jj.save()
            registered= True
        else:
            print(inst_of_user_form.errors,inst_of_profile_form.errors )
    else:
        inst_of_user_form = JoyanUserForm()
        inst_of_profile_form = JoeUserProfileInfoForm()

    contex_dict_jpj = {'jpj_user_form' :  inst_of_user_form,
                       'jj_user_prof_form' : inst_of_profile_form,
                       'josh_registered' :registered
                      }
    return render(request,'basic_app/registration.html',contex_dict_jpj )

def joe_user_login(request):
    if (request.method == 'POST'):
        joe_username = request.POST.get('username')
        # see in the login.html that the name given for field password is "joe_password"
        joe_password = request.POST.get('joe_password')

        jpj_user =authenticate(username=joe_username, password = joe_password)

        if jpj_user:
            if jpj_user.is_active:
                login(request, jpj_user)
                # see in urls.py at project level that name given for the url for index is joyan_index
                return HttpResponseRedirect(reverse('joyan_index'))
            else:
                HttpResponse("Account not active")
        else:
            print ('Some one tried to login and failed.')
            print ("user name : {} and pasword : {}".format(joe_username, joe_password))
            return HttpResponse("Invalid Log in Details")
    else:
        return render (request, 'basic_app/login.html', {})
