from django.db import models
from django.db.models import QuerySet
from django.utils.functional import cached_property

from itemsapp.models import Monitor, Printer, SysBlock, Scanner, Ups
from userapp.models import WorkUser


class ArmQuerySetManager(QuerySet):
    pass


class Arm(models.Model):
    objects = ArmQuerySetManager.as_manager()

    worker = models.ForeignKey(WorkUser, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')
    sysblock = models.ForeignKey(SysBlock, on_delete=models.SET_NULL, null=True, verbose_name='Системный блок')
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, verbose_name='Монитор')
    printer = models.ForeignKey(Printer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Принтер')
    scanner = models.ForeignKey(Scanner, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сканер')
    ups = models.ForeignKey(Ups, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='ИБП')

    @cached_property
    def __str__(self):
        return str(self.worker.workuser.select_related().all())

    class Meta:
        ordering = ('worker',)
        select_on_save = True
