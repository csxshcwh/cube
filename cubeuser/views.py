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
        form = CubeuserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cuebuser = Cubeuser()
            cuebuser.username = cleaned_data.get('username')
            cuebuser.password = make_password(cleaned_data.get('password'))
            cuebuser.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/users/regist')
