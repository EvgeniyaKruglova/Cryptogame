from django_filters import Filterset, CharFilter, DateTimeFilter
from .models import TaskCard

class TaskCardFilter(Filterset):
    creator__name = CharFilter(lookup_expr='icontains')
    published = DateTimeFilter()
    class Meta:
        model = TaskCard
        fields = ['creator', 'published']
