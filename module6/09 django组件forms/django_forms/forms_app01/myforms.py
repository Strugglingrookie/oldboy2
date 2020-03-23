from django.forms import widgets
from django import forms
from django.core.exceptions import ValidationError

wdg1 = widgets.TextInput(attrs={'class': 'form-control'})  # 可以给input标签加任何属性
wdg2 = widgets.PasswordInput(attrs={'class': 'form-control'})


class UserForms(forms.Form):  # 创建forms校验对象
    name = forms.CharField(min_length=4, max_length=8, widget=wdg1, label='姓名')  # min_length 校验规则
    pwd = forms.CharField(min_length=4, widget=wdg2, label='密码')
    r_pwd = forms.CharField(min_length=4, widget=wdg2, label='确认密码')
    email = forms.EmailField(widget=wdg1, label='邮箱')
    tel = forms.CharField(min_length=11, max_length=11, widget=wdg1, label='手机号')

    # 局部钩子
    def clean_name(self):
        val = self.cleaned_data.get('name')
        if not val.isdigit():
            return val
        else:
            raise ValidationError('用户名不能全是数字')

    # 全局钩子
    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次密码不一致!')
