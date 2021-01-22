from django.contrib import admin
from .models import Dignocis,Patient
# Register your models here.

# class ItemAdmin(admin.ModelAdmin):
#     readonly_fields = ('created',)

admin.site.register(Dignocis)
admin.site.register(Patient)