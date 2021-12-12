from django.contrib import admin
from .models import TodoModel

class TodoAdmin(admin.ModelAdmin):
	list_display = ('task','deadline','note','timestamp')
	list_filter = ('timestamp',)

admin.site.register(TodoModel)
