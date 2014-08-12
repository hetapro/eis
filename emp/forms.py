from django import forms

class NewEmpForm(forms.Form):
    ena = forms.CharField(label='Name', max_length=100)
    age = forms.CharField(label='Age', max_length=100)
    email = forms.EmailField(label='Email_id', max_length=100)
    mob=forms.CharField(label='Mob_no')
    designation = forms.CharField(label='Designation', max_length=100)

