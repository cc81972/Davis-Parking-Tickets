from django.contrib import admin
from .models import TicketInfo
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
  list_display = ("location", "date",)
  
admin.site.register(TicketInfo, TicketAdmin)