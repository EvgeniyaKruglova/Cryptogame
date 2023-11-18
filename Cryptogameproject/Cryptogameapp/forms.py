from django import forms
from .models import TaskCard


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskCard
        fields = ['card_task',
                  'taskpic',
                  'award',
                  'creator',
                  'level',
                  'type',
                  'status',
                  # 'start_time',
                  'last_date',
                  ]
        labels={
            'taskpic':'Изображение',
            'award':'Награда',
            # 'level':'Уровень',
            'type':'Тип',
            'status':'Статус',
            # 'last_date':'Дата окончания',
        }

        widgets = {
            'website': forms.URLInput
        }

