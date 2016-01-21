from django.contrib import admin
from regis.models import Register
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
	list_display = ('name','email','course','branch','contact','college','college_name','year')
	list_filter = ('email','college','branch','year')
	search_fields = ('email',)

admin.site.register(Register, RegisterAdmin)