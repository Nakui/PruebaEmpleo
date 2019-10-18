from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        #O se puede utilizar fields = '__all__'
        fields = [
            'name',
            'date_of_delivery',
            'description',
            'inCharge',
        ]

        labels = {
            'name': 'Task Name',
            'date_of_delivery': 'Date of delivery',
            'description': 'Description',
            'inCharge': 'In Charge Name',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_delivery': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'inCharge': forms.Select(attrs={'class': 'form-control'}),
        }