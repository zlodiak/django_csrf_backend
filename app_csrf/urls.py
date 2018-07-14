from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^display_form$', views.display_form, name='display_form'),
    url(r'^transfer_money$', views.transfer_money, name='transfer_money'),
]