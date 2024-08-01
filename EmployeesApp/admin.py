from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'role', 'email', 'phone_number')
    list_filter = ('role',)

admin.site.register(Employee, EmployeeAdmin)
