from django.contrib import admin
from regis.models import Participants_Details
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('name','email','course','branch','contact','college','college_name','year')
	list_filter = ('email','college','branch','year')
	search_fields = ('email',)

admin.site.register(Participants_Details, ParticipantAdmin)

