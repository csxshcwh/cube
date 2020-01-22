from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse

from .models import Cubeuser
from .forms import CubeuserForm
# Create your views here.
def regist(request):
    if request.method == 'GET':
        return render(request, 'main/regist.html')
    if request.method == 'POST':
        form = CubeuserForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cuebuser = Cubeuser()
            cuebuser.username = cleaned_data.get('username')
            cuebuser.password = make_password(cleaned_data.get('password'))
            cuebuser.truename = cleaned_data.get('truename')
            cuebuser.sex = cleaned_data.get('sex')
            cuebuser.birthday = cleaned_data.get('birthday')
            cuebuser.address = cleaned_data.get('address')
            cuebuser.email = cleaned_data.get('email')
            cuebuser.picture = cleaned_data.get('picture')
            cuebuser.emergencyname = cleaned_data.get('emergencyname')
            cuebuser.emergencyphone = cleaned_data.get('emergencyphone')
            cuebuser.save()
            return HttpResponseRedirect('/')
        else:
            errmsg = form.errors
            return render(request, 'main/regist.html', context={'error': errmsg})
