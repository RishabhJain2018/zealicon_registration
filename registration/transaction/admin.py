from django.contrib import admin
from .models import Transaction
from import_export.admin import ImportExportModelAdmin


class TransactionAdmin(ImportExportModelAdmin):
	list_display = ('username','society','jss_registration','other_registration','amount',)
	list_filter = ('username','other_registration', 'jss_registration',)
	search_fields = ('username', 'society',)
	

admin.site.register(Transaction, TransactionAdmin)
