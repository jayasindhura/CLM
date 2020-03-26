from django.conf.urls import url
from . import views
from django.urls import path, re_path
from myclm.views import *

app_name = 'myclm'
urlpatterns = [

    path("", homepage, name='homepage'),
    path('home_member/', views.home_member, name='home_member'),
    path("staff-login/", staffLogin, name='staffLogin'),
    path("member-login/", memberLogin, name='memberLogin'),
    path("staff-signup/", staffSignup, name='staffSignup'),
    path("member-signup/", memberSignup, name='memberSignup'),
    path("logout/", user_logout, name='user_logout'),

    #re_path(r'^home/$', views.home, name='home'),
    path('member_list', views.member_list, name='member_list'),
    path('member/<int:pk>/edit/', views.member_edit, name='member_edit'),
    path('member/<int:pk>/delete/', views.member_delete, name='member_delete'),
    path('borrow_list', views.borrow_list, name='borrow_list'),
    path('borrow/create/', views.borrow_new, name='borrow_new'),
    path('borrow/<int:pk>/edit/', views.borrow_edit, name='borrow_edit'),
    path('borrow/<int:pk>/delete/', views.borrow_delete, name='borrow_delete'),
    path('book_list', views.book_list, name='book_list'),
    path('book/create/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
