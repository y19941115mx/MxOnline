# -*- coding:utf-8 -*-
from django import forms
__author__ = 'victor'
__date__ = '2017/6/10 下午9:51'


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=6)
    password = forms.CharField(required=True, min_length=6)