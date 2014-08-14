from django.conf.urls import patterns,url

from emp import views

urlpatterns=patterns('',url(r'^$', views.IndexView.as_view(), name="index"),
                        url(r'^list/$', views.List.as_view(), name="List"),
                        url(r'^list1/$', views.List1.as_view(), name="List1"),
                        url(r'^new/$', 'emp.views.new', name="New"),
                        url(r'^new1/$', 'emp.views.new1', name="New1"),
                        url(r'^editDep/$', 'emp.views.editDep', name="EditD"),
                        url(r'^editemp/$', 'emp.views.editemp', name="EditEmp"),
                        url(r'^delete/(\d+)/$', 'emp.views.delete1',name="Delete"),
                        url(r'^deldep/(\d+)/$', 'emp.views.deldep',name="Deldep"),
                        url(r'^view/(\d+)/$', 'emp.views.view',name="View"),
                        url(r'^viewdetail/(\d+)/$', 'emp.views.viewdetail',name="Viewdetail"),
                        url(r'^edit1/(\d+)/$', 'emp.views.edit1',name="Edit1"),
                        url(r'^edite/(\d+)/$', 'emp.views.edite',name="Edite"),


                     )