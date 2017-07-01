# -*- coding:utf-8 -*-
__author__ = 'victor'
__date__ = '2017/7/1 下午7:33'

from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView


urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    #提交我要学习
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    #机构首页
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
]