from django.contrib import admin
from edu_web.models import Students, Curator, Discipline, Direction, Groups, MyReport

# по хорошему в админке в списках должно быть побольше данных наверное

class DirectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_dir',
        'curator',
    )
    # поясню здесь зачем это так разбивается
    # во первых читаемость
    # во вторых редактировать проще
    # в третьих когда ктот поле добавит ему будет авторство ток этого поля а не половины всех
    # в четвертых илон маск оценивает разрабов по числу строк
    list_display_links = (
        'name_dir',
        'curator', # запятая в конце тоже сам ставь не то тот кто поставит чтоб продолжить станет автором
        #и его будут бить палками вместо тебя
    )


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
admin.site.register(Groups)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Discipline)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(MyReport, MyReportAdmin)
