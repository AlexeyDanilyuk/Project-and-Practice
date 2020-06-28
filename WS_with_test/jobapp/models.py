from django.db import models
from django.db.models import QuerySet


class JobTitleQuerySetManager(QuerySet):
    pass


class JobTitle(models.Model):
    objects = JobTitleQuerySetManager.as_manager()

    job_title = models.CharField(verbose_name='Полное наименование должности', max_length=40)
    job_title_short = models.CharField(verbose_name='Сокращенное наименование должности', max_length=15)

    def __str__(self):
        return self.job_title_short

    class Meta:
        ordering = ('job_title_short',)
        select_on_save = True
