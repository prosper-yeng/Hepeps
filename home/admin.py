from django.contrib import admin
from .models import HepepsTeam,BackgroundImages
# Register your models here.

class HepepsTeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')

admin.site.register(HepepsTeam,HepepsTeamAdmin)
admin.site.register(BackgroundImages)



