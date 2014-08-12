from bsddb import db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from emp.forms import NewEmpForm
from emp.models import Emp1

class IndexView(generic.TemplateView):
    template_name = 'emp/index.html'

class List(generic.ListView):
    context_object_name = 'empl'
    template_name = 'emp/list.html'
    def get_queryset(self):
       return Emp1.objects.all()

class NewEmp(generic.TemplateView):
    template_name = 'emp/new.html'

"""class Insert(generic.ListView):

    e1=Emp1(ename= ,age= ,emailid= ,mobno= ,designation=)
    e1.save() """

def new(request):
    if request.method == 'POST':

        form = NewEmpForm(request.POST)

        if form.is_valid():
            e1=form.cleaned_data['ena']
            e2=form.cleaned_data['age']
            e3=form.cleaned_data['email']
            e4=form.cleaned_data['mob']
            e5=form.cleaned_data['designation']
            edet=Emp1.objects.create(ename=e1,age=e2,emailid=e3,mobno=e4,designation=e5)
           # return render(request,'emp')
    else:
        form = NewEmpForm()

    return render(request, 'emp/new.html', {'form': form})

def delete(request, id):
   e1= Emp1.objects.get(pk=id)
   e1.delete()
   return render(request,'emp/delete.html')