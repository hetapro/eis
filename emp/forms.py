from django import forms
from emp.models import Dep

class NewEmpForm(forms.Form):
    ena = forms.CharField(label='Name', max_length=100)
    age = forms.CharField(label='Age', max_length=100)
    email = forms.EmailField(label='Email id', max_length=100)
    mob=forms.CharField(label='Mob no')
    designation = forms.CharField(label='Designation', max_length=100)
    department=forms.ModelChoiceField(label='Department',queryset=Dep.objects.all(), to_field_name='dept',empty_label="select")

class NewDepForm(forms.Form):
    d1 = forms.CharField(label='Department Name', max_length=100)
