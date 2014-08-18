from bsddb import db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from emp.forms import NewEmpForm, NewDepForm
from emp.models import Emp1, Dep

class IndexView(generic.TemplateView):
    template_name = 'emp/index.html'

class List(generic.ListView):
    context_object_name = 'empl'
    template_name = 'emp/list.html'
    def get_queryset(self):
       return Emp1.objects.all()

class List1(generic.ListView):
    context_object_name = 'depl'
    template_name = 'emp/list1.html'
    def get_queryset(self):
       return Dep.objects.all()

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
            edet=Emp1.objects.create(ename=e1,age=e2,emailid=e3,mobno=e4,designation=e5,dep=e6)
            return HttpResponseRedirect(reverse('emp:List'))
    else:
        form = NewEmpForm()

    return render(request, 'emp/new.html', {'form': form, 'd1': Dep.objects.all()})


def new1(request):
    if request.method == 'POST':

        form = NewDepForm(request.POST)

        if form.is_valid():
            d1=form.cleaned_data['d1']
            det=Dep.objects.create(dept=d1)
            return HttpResponseRedirect(reverse('emp:List1'))
    else:
        form = NewDepForm()

    return render(request, 'emp/new1.html', {'form': form})

def view(request,id):
   e2=get_object_or_404(Emp1,pk=id)
   return render(request,'emp/view.html', {'e2': e2})

def delete1(request, id):
   e1= Emp1.objects.get(pk=id)
   e1.delete()
   return HttpResponseRedirect(reverse('emp:List'))
 #  return render(request, 'emp/list.html', {'emp':e1, 'del1_message': "Record succesfully deleted.",})

def deldep(request, id):
    d1=Dep.objects.get(pk=id)
    d1.delete()
    return HttpResponseRedirect(reverse('emp:List1'))

def viewdetail(request, id):
    e3=Emp1.objects.filter(dep=id)
    return render(request,'emp/view1.html', {'e3': e3})

def edit1(request,id):
    d1=Dep.objects.get(pk=id)
    return render(request, 'emp/edit1.html', {'d1': d1})

def edite(request,id):
    e1=Emp1.objects.get(pk=id)
    d1=Dep.objects.all()
    return render(request, 'emp/edite.html', {'d1': d1, 'e1': e1})

def editDep(request):
    name = request.GET.get('dept')
    id1 = request.GET.get('deid')
    d1 = Dep.objects.get(pk=id1)
    departments=Dep.objects.all()
    flag=False
    for d in departments:
        if name==d.dept:
            flag=True

    if flag:
        return render(request, 'emp/edit1.html', {'d1': d1, 'error_message':'This department already exists.!!'})
    else:
       d1.dept = name
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
    id=Dep.objects.get(dept=name5)
    e1 = Emp1.objects.get(pk=id1)
    e1.ename = name; e1.age=name1; e1.emailid=name2; e1.mobno=name3; e1.designation=name4; e1.dep_id=id;
    e1.save()
    return HttpResponseRedirect(reverse('emp:List'))






