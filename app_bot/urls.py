from django.conf.urls import url
from . import views

urlpatterns = [
        
        url(r'^message$', views.message),
        url(r'^keyboard$', views.key),
        url(r'^friend$', views.friend),

        
        
        ]
