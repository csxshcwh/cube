from django.shortcuts import render
from django.http import HttpResponseRedirect

from cubeuser.models import Cubeuser
from .forms import LoginForm
# Create your views here.


def index(request):
    if request.session.get('is_login') is None:
        sesuser = 0
    else:
        email = request.session.get('user_email')
        sesuser = Cubeuser.objects.get(email=email)

    context = {
        'cubeuser': sesuser
    }
    return render(request, 'main/index.html', context=context)


def login(request):
    if request.session.get('is_login', None):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            user = Cubeuser.objects.get(email=email)

            request.session['is_login'] = True
            request.session['user_id'] = user.username
            request.session['user_email'] = user.email
            return HttpResponseRedirect('/')
        else:
            errmsg = login_form.errors
            elmsg = login_form.non_field_errors()
            context = {
                'error': errmsg,
                'elerr': elmsg
            }
            return render(request, 'main/login.html', context=context)

    context = {

    }
    return render(request, 'main/login.html', context=context)


def logout(request):
    if request.session.get('is_login') is None:
        return HttpResponseRedirect("/")
    request.session.flush()
    return HttpResponseRedirect("/")

