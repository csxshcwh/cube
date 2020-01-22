from django import forms
from django.contrib.auth.hashers import make_password

from .models import Cubeuser


class CubeuserForm(forms.Form):
    username = forms.CharField(label='用户名', error_messages={'required': u'用户名'})
    password = forms.CharField(label='密码', error_messages={'required': u'密码'})
    repwd = forms.CharField(label='确认密码', error_messages={'required': u'确认密码'})
    truename = forms.CharField(label='真实姓名', error_messages={'required': u'真实姓名'})
    sex = forms.ChoiceField(choices=Cubeuser.SEX_ITEMS, label='性别', error_messages={'required': u'性别'})
    birthday = forms.DateField(label='出生日期', error_messages={'required': u'出生日期'})
    address = forms.CharField(label='邮寄地址', error_messages={'required': u'邮寄地址'})
    email = forms.EmailField(label='邮箱', error_messages={'required': u'邮箱'})
    picture = forms.ImageField(label='图片', error_messages={'required': u'图片'})
    emergencyname = forms.CharField(label='紧急联络人姓名', error_messages={'required': u'紧急联络人姓名'})
    emergencyphone = forms.CharField(label='紧急联络人电话', error_messages={'required': u'紧急联络人电话'})

    def clean_truename(self):
        cleaned_data = self.cleaned_data.get('truename')
        return cleaned_data

    def clean_picture(self):
        cleaned_data = self.cleaned_data.get('picture')
        print(cleaned_data)
        return cleaned_data

    def clean(self):
        password = self.cleaned_data.get('password')
        repwd = self.cleaned_data.get('repwd')
        if password == repwd:
            pass
        else:
            raise forms.ValidationError('输入不一致！')

