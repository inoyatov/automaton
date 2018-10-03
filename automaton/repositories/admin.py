from django.contrib import admin

from .models import Repositories

class RepositoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'creator', 'created', 'modified')

admin.site.register(Repositories, RepositoriesAdmin)
