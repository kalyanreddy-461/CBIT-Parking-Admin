from django.urls import path

from . import views

urlpatterns = [
    path('base',views.base,name='base'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dismiss',views.dismiss,name='dismiss'),
    path('fines',views.fines,name='fines'),
    path('fine',views.fine,name='fine'),
    path('regstatistics',views.regstatistics,name='regstatistics'),
    path('paystatistics',views.paystatistics,name='paystatistics')
]
