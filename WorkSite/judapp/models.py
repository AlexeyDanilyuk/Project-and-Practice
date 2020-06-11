from django.db import models
from django.db.models import QuerySet


class JudSiteQuerySetManager(QuerySet):
    pass


class JudSite(models.Model):
    objects = JudSiteQuerySetManager.as_manager()
    jud_site = models.CharField(verbose_name='Полное наименование СУ', max_length=150)
    jud_site_short = models.CharField(verbose_name='Сокращенное наименование СУ', max_length=25)

    def __str__(self):
        return self.jud_site_short

    class Meta:
        ordering = ('jud_site_short',)
        select_on_save = True
