#Custom Filters

import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name = 'designation', lookup_expr='iexact')  #iexact accept both lower and uppercase
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')       #icontains fiters if give john will give all names cotains john
    # emp_id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From emp_id')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To emp_id')
    
    class Meta:
        model = Employee
        fields = ['designation', 'emp_name','id_min','id_max']
        
    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte = value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte = value)
        else:
            return queryset
        
