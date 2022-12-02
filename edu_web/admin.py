from django.contrib import admin
from edu_web.models import Students, Curator, Discipline, Direction, Groups
from edu_web.report.models_rep import MyReport


class DirectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_dir',
        'curator',
    )
    list_display_links = (
        'id',
        'name_dir',
        'curator',
    )

class DisciplineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_dis',
        'direction',
    )
    list_display_links = (
        'id',
        'name_dis',
        'direction',
    )

class GroupsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'group_name',
        'group_number',
        'max_number_students',
        'direction',
    )
    list_display_links = (
        'id',
        'group_name',
        'group_number',
        'max_number_students',
        'direction',
    )



class CuratorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'middle_name',
        'last_name',
        'phone_number',
        'mail_address',
        'user',
    )
    list_display_links = (
        'id',
        'first_name',
        'middle_name',
        'last_name',
        'phone_number',
        'mail_address',
        'user',
    )


class StudentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'group',
    )
    list_display_links = (
        'id',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'group',
    )

class MyReportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file_name',
        'datatime_created',
        'rep_status',
    )
    list_display_links =(
        'id',
        'file_name',
        'datatime_created',
        'rep_status',
    )


admin.site.register(Students, StudentsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(MyReport, MyReportAdmin)
