from django.contrib import admin
from regis.models import Participants_Details, Participants_Online
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('name','email','course','branch','contact','college','year',)
	list_filter = ('email','college','branch','year',)
	search_fields = ('email',)


class ParticipantOnline(admin.ModelAdmin):
	list_display = ('zealid','name','email','course','branch','contact','college','year',)
	list_filter = ('email','college','branch','year',)
	search_fields = ('email',)
	

admin.site.register(Participants_Details, ParticipantAdmin)
admin.site.register(Participants_Online, ParticipantOnline)

