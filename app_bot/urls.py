from django.conf.urls import url,handler404
from . import views

urlpatterns = [
        
        url(r'^message$', views.message),
        url(r'^keyboard$', views.key),
        url(r'^friend', views.friend),
        url(r'^chat_room', views.chat_room),

        #url(r'^/', views.error_404),

        
        
        ]

handler404 = views.error404
