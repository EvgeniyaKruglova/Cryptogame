from django_filters import FilterSet, CharFilter, DateTimeFilter
from .models import TaskCard

class TaskCardFilter(FilterSet):
    creator = CharFilter(lookup_expr='icontains')
    published = DateTimeFilter()
    class Meta:
        model = TaskCard
        fields = ['creator', 'published']
