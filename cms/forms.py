from django import forms
from django.forms import ModelForm
from .models import Dignocis, Patient, Docter
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age',]


class DocterForm(ModelForm):
    class Meta:
        model = Docter
        fields = ['name', 'age', 'position', 'email']



class DignosisForm(ModelForm):
    class Meta:
        model = Dignocis
        fields = ['symptoms', 'medcines', 'name','patient',]

