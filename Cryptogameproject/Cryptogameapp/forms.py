from django import forms
from .models import TaskCard, CategoryTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskCard
        fields = ('name', 'description', 'category', 'website',)
        widgets = {
            'website': forms.URLinput
        }
