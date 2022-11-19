from time import sleep
from django.utils.datetime_safe import datetime

from educational_process.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# @app.task()
# def test_cel(b=2, c=6):
#     result = b + c
#     return result
@app.task(bind=True)
def report_create(*args, **kwargs, ):
    logger.info('Проверка')
    logger.info(str(kwargs) + str(args))
    from edu_web.models import Direction, Discipline, Curator, Students
    from edu_web.models import MyReport
    task = MyReport.objects.get()
    task.rep_status = 0
    task.save()
    queryset = Students.objects.select_related('group__curator'). \
        prefetch_related('group__disciplines__direction')
    print(queryset)
    file_name = 'report.xlsx'
    for student in queryset:
        print(student, student.group, student.group.curator,)
        for discipline in student.group.disciplines.all():
            print(discipline, discipline.direction)
    # with open(file_name, 'w') as f:
    #     for d in queryset:
    #         print(d, file=f)
    # for u in discipline_queryset:
    #     print(u.name_dis, file=f)
    # for c in curator_queryset:
    #     print(c.first_name,c.middle_name, c.last_name, file=f)

    task.file_name = file_name
    task.rep_status = 2
    task.save()
