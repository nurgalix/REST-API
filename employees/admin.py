from django.contrib import admin

from employees.models import Employees, Category

admin.site.register(Employees)
admin.site.register(Category)