# -*- coding:utf-8 -*-
__author__ = 'victor'
__date__ = '2017/7/1 下午7:33'

from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView,\
    OrgDescView, OrgTeacherView, AddFavView


urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    #提交我要学习
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    #机构首页
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    #机构课程页
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    #机构介绍页
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    #机构教师页
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),
    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]