from django.conf.urls import patterns, url
from demo.celeryapp import views

urlpatterns = patterns('', 
	url(r'^$', views.add_stool_record, name="addstool"),

)