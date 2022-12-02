from django.contrib import admin
from edu_web.models import Students, Curator, Discipline, Direction, Groups
from edu_web.report.models_rep import MyReport


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_dir', 'curator')
    list_display_links = ('name_dir', 'curator')

class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name',)



class MyReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'datatime_created', 'rep_status', )
    list_display_links = ('id', )


class CuratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name',
                    'phone_number', 'mail_address')
    list_display_links = ('first_name', 'middle_name', 'last_name',
                          'phone_number', 'mail_address')


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name',
                    'gender', 'group')
    list_display_links = ('gender', 'group')


admin.site.register(Students, StudentsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Discipline)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(MyReport, MyReportAdmin)
