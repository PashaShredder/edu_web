from django.db import models
from edu_web.report.tasks import report_create

class MyReport(models.Model):
    NOT_STARTED = 0
    DURING = 1
    DONE = 2
    PROCESS_CHOICES = (
        (NOT_STARTED, 'not_started'),
        (DURING, 'during'),
        (DONE, 'done'),
    )
    file_name = models.CharField(
        max_length=150,
        verbose_name='Имя отчёта',
    )
    datatime_created = models.DateTimeField(
        auto_now_add=True,
    )
    rep_status = models.IntegerField(
        default=NOT_STARTED,
        choices=PROCESS_CHOICES,
    )

    def __str__(self):
        return f'{self.file_name}'


    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save()
            report_id = self.pk
            report_create.delay(report_id)
        else:
            super().save()