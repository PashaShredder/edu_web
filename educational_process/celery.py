import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educational_process.settings')

app = Celery('educational_process')
CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {self.request!r}'.format(self=self))
