from django.contrib import admin

# Register your models here.

from .models import Employee, BlogPost

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
admin.site.register(Employee, EmployeeAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'featured')
admin.site.register(BlogPost, BlogPostAdmin)
