from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
  list_display =('emp_name','emp_id')
  
# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
