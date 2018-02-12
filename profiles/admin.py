from django.contrib import admin
from profiles.models import UserDetail
from import_export.admin import ImportExportModelAdmin


class UserDetailAdmin(ImportExportModelAdmin):
    list_display = ('user','contact_no','college_society','year','branch','univ_roll_no',)
    list_filter = ('college_society', 'branch')
    search_fields = ('user__username', 'contact_no', 'univ_roll_no', 'year', 'college_society',)


admin.site.register(UserDetail, UserDetailAdmin)
