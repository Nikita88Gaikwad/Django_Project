from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_by', 'created_at', 'updated_at')
    search_fields = ('client_name', 'created_by__username')
