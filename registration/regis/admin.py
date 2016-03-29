from django.contrib import admin
from regis.models import ParticipantsDetail, ParticipantsOnline
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('name','email','course','branch','contact','college','year','zeal_id','fee','id_card_print','receipt_print',)
	list_filter = ('email','college','branch','year',)
	search_fields = ('email',)


class ParticipantOnline(admin.ModelAdmin):
	list_display = ('zeal_id_temp','name','email','course','branch','contact','college','year',)
	

admin.site.register(ParticipantsDetail, ParticipantAdmin)
admin.site.register(ParticipantsOnline, ParticipantOnline)
