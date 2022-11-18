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
def report_create(*args, **kwargs):
    logger.info('Kartoshka')
    logger.info(str(kwargs) + str(args))
    from edu_web.models import MyReport
    task = MyReport.objects.filter(pk=1).get()
    task.rep_status = 1
    task.save()
    from edu_web.models import Direction
    direction_queryset = Direction.objects.all()
    file_name =  'report.xlsx'

    with open(file_name, 'w') as f:
        for d in direction_queryset:
            print(d.name_dir, file=f)

    task.file_name = file_name
    task.rep_status = 2
    task.save()
