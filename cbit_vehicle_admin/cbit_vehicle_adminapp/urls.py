from django.urls import path

from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('dismiss',views.dismiss,name='dismiss'),
    path('fines',views.fines,name='fines'),
    path('statistics',views.statistics,name='statistics')
]