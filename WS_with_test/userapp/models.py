from django.db import models
from django.db.models import QuerySet

from judapp.models import JudSite
from jobapp.models import JobTitle


class WorkUserQuerySetManager(QuerySet):
    pass


class WorkUser(models.Model):
    objects = WorkUserQuerySetManager.as_manager()

    job_title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, verbose_name='Должность', null=True)
    jud_site = models.ForeignKey(JudSite, on_delete=models.SET_NULL, verbose_name='Наименование СУ', null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    patronymic = models.CharField(verbose_name='Отчество', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    num_office = models.CharField(verbose_name='Номер кабинета', max_length=3)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} ({self.job_title})"

    class Meta:
        ordering = ('jud_site', 'last_name', 'first_name',)
        select_on_save = True
