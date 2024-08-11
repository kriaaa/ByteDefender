from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
urlpatterns=[
    # path('',views.contact,name='contact'),
    path('',views.homepage,name='home'),
    path('home/',views.homepage,name='home'),
    path('check/',views.check,name='check'),
    path('login/',views.loginpage,name='login'),
    path('contact/',views.contactus,name='contact'),
     path('about/',views.about,name='about'),
    path('sign/',views.signup,name='sign'),
    path('help/',views.help, name='help'),

    path('scan/',views.upload_file,name='scan'),
    path('rocket/', views.rocket_page, name='rocket'),

]
