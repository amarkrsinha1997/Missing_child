from django.conf.urls import url,include
from . import views
from .forms import CustomAutoForm
from django.contrib.auth import views as auth_views
urlpatterns = [

  url(r'^$', views.home,name='home'),
  url(r'^login/$',auth_views.login, name='login', kwargs={"authentication_form":CustomAutoForm}),
  url(r'^logout/$',auth_views.logout, name='logout'),
  url(r'^signup/$',views.signup, name='signup'),
  url(r'^upload/$',views.upload,name="upload"),
  url(r'^report/$',views.report,name="report"),

 ]
