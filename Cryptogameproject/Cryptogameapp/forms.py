from django import forms
from .models import TaskCard


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskCard
        fields = ['name',
                  'description',
                  'taskpic',
                  'award',
                  'level',
                  'type',
                  'status',
                  'beginning_date',
                  # 'last_date ',
                  ]
        labels={
            'name':'Название',
            'description':'Описание',
            'taskpic':'Изображение',
            'award':'Награда',
            'level':'Уровень',
            'type':'Тип',
            'status':'Статус',
            'beginning_date':'Дата начала',
            # 'last_date':'Дата окончания',
        }

        widgets = {
            'website': forms.URLInput
        }

