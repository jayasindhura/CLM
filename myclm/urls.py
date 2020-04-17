from django.conf.urls import url
from . import views
from django.urls import path, re_path
from myclm.views import *

app_name = 'myclm'
urlpatterns = [

    path("", homepage, name='homepage'),
    path('home_member/', views.home_member, name='home_member'),
    path('home_staff/', views.home_staff, name='home_staff'),

    path("staff-login/", staffLogin, name='staffLogin'),
    path("member-login/", memberLogin, name='memberLogin'),

    path("staff-signup/", staffSignup, name='staffSignup'),
    path("member-signup/", memberSignup, name='memberSignup'),

    path("logout/", user_logout, name='user_logout'),

    re_path(r'^home/$', views.home, name='home'),
    path('member_list', views.member_list, name='member_list'),
    path('member_list_staff', views.member_list_staff, name='member_list_staff'),

    path('member_staff/create/', views.member_new_staff, name='member_new_staff'),

    path('member/<int:pk>/edit/', views.member_edit, name='member_edit'),
    path('member_staff/<int:pk>/edit/', views.member_edit_staff, name='member_edit_staff'),

    path('member/<int:pk>/delete/', views.member_delete, name='member_delete'),
    path('member_staff/<int:pk>/delete/', views.member_delete_staff, name='member_delete_staff'),

    path('borrow_list', views.borrow_list, name='borrow_list'),
    path('borrow_list_staff', views.borrow_list_staff, name='borrow_list_staff'),

    path('borrow/create/', views.borrow_new, name='borrow_new'),
    path('borrow_staff/create/', views.borrow_new_staff, name='borrow_new_staff'),

    path('borrow/<int:pk>/edit/', views.borrow_edit, name='borrow_edit'),
    path('borrow_staff/<int:pk>/edit/', views.borrow_edit_staff, name='borrow_edit_staff'),

    path('borrow/<int:pk>/delete/', views.borrow_delete, name='borrow_delete'),
    path('borrow_staff/<int:pk>/delete/', views.borrow_delete_staff, name='borrow_delete_staff'),

    path('book_list', views.book_list, name='book_list'),
    path('book_list_staff', views.book_list_staff, name='book_list_staff'),

    path('book/create/', views.book_new, name='book_new'),
    path('book_staff/create/', views.book_new_staff, name='book_new_staff'),

    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book_staff/<int:pk>/edit/', views.book_edit_staff, name='book_edit_staff'),

    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('book_staff/<int:pk>/delete/', views.book_delete_staff, name='book_delete_staff'),

    path('pdf/', views.borrow_summary_pdf,name='borrow_summary_pdf'),

    #path('borrow_summary_pdf', views.borrow_summary_pdf, name='borrow_summary_pdf'),

    #path('borrow_summary_pdf', views.get, name='borrow_summary_pdf'),
]
