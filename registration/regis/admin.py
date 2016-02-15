from django.contrib import admin
from regis.models import Participants_Details, Participants_Online
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('name','email','course','branch','contact','college','year','zealidfinal',)
	list_filter = ('email','college','branch','year',)
	search_fields = ('email',)


class ParticipantOnline(admin.ModelAdmin):
	list_display = ('zealid','name','email','course','branch','contact','college','year',)
	

admin.site.register(Participants_Details, ParticipantAdmin)
admin.site.register(Participants_Online, ParticipantOnline)
