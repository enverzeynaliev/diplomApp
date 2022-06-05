from django.contrib import admin
from .models import departments, course_on_categories
# Register your models here.

admin.site.register(departments)
admin.site.register(course_on_categories)