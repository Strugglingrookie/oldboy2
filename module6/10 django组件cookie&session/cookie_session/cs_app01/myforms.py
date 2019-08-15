from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from cs_app01.models import UserInfo


name_widg = widgets.TextInput(attrs={'class':'form-control'})
pwd_widg = widgets.PasswordInput(attrs={'class':'form-control'})
class Myform(forms.Form):
    name = forms.CharField(min_length=4, max_length=32, widget=name_widg, label="用户名")
    pwd = forms.CharField(min_length=4, widget=pwd_widg, label="密码")

    def clean_name(self):
        val = self.cleaned_data.get('name')
        res = UserInfo.objects.filter(name=val).exists()
        if res:
           return val
        else:
            raise ValidationError('用户名不存在！')

    def clean(self):
        name = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('pwd')
        print(name, pwd)
        res = UserInfo.objects.filter(name=name, pwd=pwd).exists()
        if res:
            return self.cleaned_data
        else:
            raise ValidationError('密码不正确！')