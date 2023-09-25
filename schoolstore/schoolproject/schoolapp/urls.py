from .import views
from django.urls import path


urlpatterns=[

    path('',views.index,name='home'),

    path('contact/',views.contact,name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new_page/', views.new_page, name='new_page'),

]