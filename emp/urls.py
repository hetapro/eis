from django.conf.urls import patterns,url

from emp import views

urlpatterns=patterns('',url(r'^$', views.IndexView.as_view(), name="index"),
                        url(r'^list/$', views.List.as_view(), name="List"),
                        url(r'^new/$', 'emp.views.new', name="New"),
                        url(r'^delete/(\d+)/$', 'emp.views.delete',name="delete")
                     )