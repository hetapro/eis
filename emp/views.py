from bsddb import db
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware import csrf
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from emp.forms import NewEmpForm, NewDepForm
from emp.models import Employee,Department
from emp.serializers import DepSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,action,link
from rest_framework.decorators import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import renderers
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.request import Request

class Department_List(viewsets.ModelViewSet):
    model = Department
    queryset = Department.objects.all()
    serializer_class = DepSerializer

class Employee_List(viewsets.ModelViewSet):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class IndexView(generic.TemplateView):

    template_name = 'emp/index.html'

class List(generic.ListView):
    context_object_name = 'empl'
    template_name = 'emp/list.html'
    def get_queryset(self):
       return Employee.objects.all()

class List1(generic.ListView):
    context_object_name = 'depl'
    template_name = 'emp/list1.html'
    def get_queryset(self):
       return Department.objects.all()

def new(request):
    if request.method == 'POST':

        form = NewEmpForm(request.POST)

        if form.is_valid():
            e1=form.cleaned_data['ena']
            e2=form.cleaned_data['age']
            e3=form.cleaned_data['email']
            e4=form.cleaned_data['mob']
            e5=form.cleaned_data['designation']
            e6=form.cleaned_data['department']
            edet=Employee.objects.create(ename=e1,age=e2,emailid=e3,mobno=e4,designation=e5,department=e6)
            return HttpResponseRedirect(reverse('emp:List'))
    else:
        form = NewEmpForm()

    return render(request, 'emp/new.html', {'form': form, 'd1': Department.objects.all()})


def new1(request):
    if request.method == 'POST':

        form = NewDepForm(request.POST)

        if form.is_valid():
            d1=form.cleaned_data['d1']
            det=Department.objects.create(department_name=d1)
            return HttpResponseRedirect(reverse('emp:List1'))
    else:
        form = NewDepForm()

    return render(request, 'emp/new1.html', {'form': form})

def view(request,id):
   e2=get_object_or_404(Employee,pk=id)
   return render(request,'emp/view.html', {'e2': e2})

def delete1(request, id):
   e1= Employee.objects.get(pk=id)
   e1.delete()
   return HttpResponseRedirect(reverse('emp:List'))
 #  return render(request, 'emp/list.html', {'emp':e1, 'del1_message': "Record succesfully deleted.",})

def deldep(request, id):

    d1=Department.objects.get(pk=id)
    d1.delete()
    return HttpResponseRedirect(reverse('emp:List1'))

def viewdetail(request, id):
    e3=Employee.objects.filter(department=id)
    return render(request,'emp/view1.html', {'e3': e3, 'department':Department.objects.get(pk=id)})

def edit1(request,id):
    d1=Department.objects.get(pk=id)
    return render(request, 'emp/edit1.html', {'d1': d1})

def edite(request,id):
    e1=Employee.objects.get(pk=id)
    d1=Department.objects.all()
    return render(request, 'emp/edite.html', {'d1': d1, 'e1': e1})

def editDep(request):
    name = request.GET.get('dept')
    id1 = request.GET.get('deid')
    d1 = Department.objects.get(pk=id1)
    departments=Department.objects.all()
    flag=False
    for d in departments:
        if name==d.department_name:
            flag=True

    if flag:
        return render(request, 'emp/edit1.html', {'d1': d1, 'error_message':'This department already exists.!!'})
    else:
       d1.department_name = name
       d1.save()
       return HttpResponseRedirect(reverse('emp:List1'))

def editemp(request):
    name = request.GET.get('e2')
    name1 = request.GET.get('e3')
    name2 = request.GET.get('e4')
    name3 = request.GET.get('e5')
    name4 = request.GET.get('e6')
    name5 = request.GET.get('e7')
    id1 = request.GET.get('eeid')
    id=Department.objects.get(department_name=name5)
    e1 = Employee.objects.get(pk=id1)
    e1.ename = name; e1.age=name1; e1.emailid=name2; e1.mobno=name3; e1.designation=name4; e1.department_id=id;
    e1.save()
    return HttpResponseRedirect(reverse('emp:List'))






