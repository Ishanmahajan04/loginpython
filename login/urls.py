from django.conf.urls import url
from . import views


urlpatterns = [
 url(r'^$',views.index,name='index'),
 url(r'^k/$',views.loginapp ,name='loginapp')
]
