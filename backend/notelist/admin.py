from django.contrib import admin
from .models import Notelist

class ListAdmin(admin.ModelAdmin):
    list_display = ('task', 'description', 'completed', 'created')

# Register your models here.

admin.site.register(Notelist, ListAdmin)


