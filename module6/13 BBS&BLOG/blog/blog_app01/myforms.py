from django.forms import widgets
from django import forms
from django.core.exceptions import ValidationError
from blog_app01.models import UserInfo


wdg1 = widgets.TextInput(attrs={'class':'form-control'})  # 可以给input标签加任何属性
wdg2 = widgets.PasswordInput(attrs={'class':'form-control'})
class UserForms(forms.Form):  # 创建forms校验对象
    name = forms.CharField(min_length=4, max_length=8,widget=wdg1, label='用户名') # min_length 校验规则
    pwd = forms.CharField(min_length=4,widget=wdg2, label='密码')
    r_pwd = forms.CharField(min_length=4,widget=wdg2, label='确认密码')
    email = forms.EmailField(widget=wdg1, label='邮箱')
    tel = forms.CharField(min_length=11, max_length=11,widget=wdg1, label='手机号')

    #局部钩子
    def clean_name(self):
        val = self.cleaned_data.get('name')
        res = UserInfo.objects.filter(username=val).exists()
        if not res:
            return val
        else:
            raise ValidationError('用户名已存在！')

    def clean_tel(self):
        val = self.cleaned_data.get('tel')
        res = UserInfo.objects.filter(phone_num=val).exists()
        if not res:
            return val
        else:
            raise ValidationError('手机号已存在！')

    def clean_email(self):
        val = self.cleaned_data.get('tel')
        res = UserInfo.objects.filter(email=val).exists()
        if not res:
            return val
        else:
            raise ValidationError('邮箱已存在！')

    # 全局钩子
    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次密码不一致!')

