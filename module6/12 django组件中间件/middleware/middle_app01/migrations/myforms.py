from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


name_widget = widgets.TextInput(attrs={'class':'form-control'})
pwd_widget = widgets.PasswordInput(attrs={'class':'form-control'})


class Form(forms.Form):
    name = forms.CharField(min_length=4, max_length=16, widget=name_widget, label='用户名')
    pwd = forms.CharField(min_length=4, max_length=16, widget=pwd_widget, label='密码')
    email = forms.EmailField(widget=name_widget, label='邮箱')

    def clean_name(self):
        val = self.cleaned_data.get('name')
        res = User.objects.filter(username=val).exists()
        if not res:
            return val
        else:
            raise ValidationError('用户名已存在！')


class LoginForm(forms.Form):
    name = forms.CharField(min_length=4, max_length=16, widget=name_widget, label='用户名')
    pwd = forms.CharField(min_length=4, max_length=16, widget=pwd_widget, label='密码')


