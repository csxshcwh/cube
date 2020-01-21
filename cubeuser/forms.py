from django import forms
from django.contrib.auth.hashers import make_password

from .models import Cubeuser


class CubeuserForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码')
    repwd = forms.CharField(label='确认密码')

    def clean(self):
        password = self.cleaned_data.get('password')
        repwd = self.cleaned_data.get('repwd')
        if password == repwd:
            pass
        else:
            raise forms.ValidationError('输入不一致！')

