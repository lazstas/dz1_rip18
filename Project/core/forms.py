from django import forms
from django.forms import ModelForm
from .models import Computer
from django.contrib.auth.models import User


class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = ['name', 'description', 'image', 'price', 'active']
