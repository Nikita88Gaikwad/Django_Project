from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_by', 'created_at')
    search_fields = ('project_name', 'client__client_name', 'created_by__username')
