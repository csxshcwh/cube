from django import forms
from django.contrib.auth.hashers import check_password

from cubeuser.models import Cubeuser


class LoginForm(forms.Form):
    email = forms.EmailField(label='邮箱', error_messages={'required': u'邮箱'})
    password = forms.CharField(label='密码', error_messages={'required': u'密码'})

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = Cubeuser.objects.get(email=email)
        except:
            raise forms.ValidationError('无该邮箱注册的用户，请先注册！')
        if check_password(password, user.password):
            pass
        else:
            raise forms.ValidationError('密码错误！')

