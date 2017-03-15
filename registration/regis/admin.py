from django.contrib import admin
from regis.models import ParticipantsDetail, ParticipantsOnline
from import_export.admin import ImportExportModelAdmin


class ParticipantAdmin(ImportExportModelAdmin):
	list_display = ('name','email','course','branch','contact','college','year','zeal_id','fee','id_card_print','receipt_print','created_by',)
	list_filter = ('email','college','branch','year','created_by',)
	search_fields = ('name', 'email', 'contact', 'zeal_id', 'created_by__username',)


class ParticipantOnline(ImportExportModelAdmin):
	list_display = ('zeal_id_temp','name','email','course','branch','contact','college','year',)
	

admin.site.register(ParticipantsDetail, ParticipantAdmin)
admin.site.register(ParticipantsOnline, ParticipantOnline)
