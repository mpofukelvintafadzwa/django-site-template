from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postemail$', views.addInterestedEmail, name='addemail'),
    url(r'^tech$', views.tech, name='tech'),
    url(r'^openaccess$', views.openAccess, name='openaccess'),
    url(r'^theteam$', views.team, name='team'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^faq$', views.faq, name='faq'),
]