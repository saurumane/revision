from django.contrib import admin
from .models import Userinputmodel
# Register your models here.
class Useradmin(admin.ModelAdmin):
    list_display = []
admin.site.register(Userinputmodel,Useradmin)