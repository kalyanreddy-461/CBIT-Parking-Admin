from django.urls import path

from . import views

urlpatterns = [
    path('base',views.base,name='base'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dismiss',views.dismiss,name='dismiss'),
    path('dismiss1',views.dismiss1,name='dismiss1'),
    path('dismiss2',views.dismiss2,name='dismiss2'),
    path('listdismiss',views.listdismiss,name='listdismiss'),
    path('fines',views.fines,name='fines'),
    path('fine',views.fine,name='fine'),
    path('regstatistic',views.regstatistic,name='regstatistic'),
    path('paystatistic',views.paystatistic,name='paystatistic'),
    path('regstatistics',views.regstatistics,name='regstatistics'),
    path('paystatistics',views.paystatistics,name='paystatistics'),

]
