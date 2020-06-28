from datetime import date
from django.db import models
from django.db.models import QuerySet
from django.utils.functional import cached_property

from userapp.models import WorkUser


class SysBlockQuerySetManager(QuerySet):
    pass


class SysBlock(models.Model):
    objects = SysBlockQuerySetManager.as_manager()

    motherboard = models.CharField(verbose_name='Материнская плата', max_length=30)
    processor = models.CharField(verbose_name='Процессор', max_length=30)
    hdd = models.CharField(verbose_name='Жесткий диск', max_length=30)
    ram = models.CharField(verbose_name='ОЗУ', max_length=10)
    inv_num = models.CharField(verbose_name='Инвентарный номер', max_length=15)
    os = models.CharField(verbose_name='Операционная система', max_length=30)
    date_mfd = models.DateField(verbose_name='Дата выпуска', default=date.today, blank=True)
    date_exp = models.DateField(verbose_name='Дата ввода в эксплуатацию', default=date.today, blank=True)
    owner = models.ForeignKey(WorkUser, related_name='sysblockitem', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Инвентарный номер: {self.inv_num} ({self.motherboard}, {self.processor}, {self.hdd}, {self.ram})"

    @cached_property
    def get_items_cached(self):
        return self.owner.workuser.select_related().all()

    class Meta:
        select_on_save = True


class MonitorQuerySetManager(QuerySet):
    pass


class Monitor(models.Model):
    objects = MonitorQuerySetManager.as_manager()

    firm_monitor = models.CharField(verbose_name='Производитель и модель монитора', max_length=20)
    diag = models.CharField(verbose_name='Диагональ', max_length=5)
    inv_num = models.CharField(verbose_name='Инвентарный номер', max_length=15)
    date_mfd = models.DateField(verbose_name='Дата выпуска', default=date.today, blank=True)
    date_exp = models.DateField(verbose_name='Дата ввода в эксплуатацию', default=date.today, blank=True)
    owner = models.ForeignKey(WorkUser, related_name='monitoritem', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firm_monitor} (Инвентарный номер: {self.inv_num})"

    class Meta:
        select_on_save = True


class UpsQuerySetManager(QuerySet):
    pass


class Ups(models.Model):
    objects = UpsQuerySetManager.as_manager()

    firm_ups = models.CharField(verbose_name='Производитель и модель ИБП', max_length=20)
    power = models.CharField(verbose_name='Мощность (ВА)', max_length=5)
    inv_num = models.CharField(verbose_name='Инвентарный номер', max_length=15)
    date_mfd = models.DateField(verbose_name='Дата выпуска', default=date.today, blank=True)
    date_exp = models.DateField(verbose_name='Дата ввода в эксплуатацию', default=date.today, blank=True)
    owner = models.ForeignKey(WorkUser, related_name='upsitem', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firm_ups} (Инвентарный номер: {self.inv_num})"

    class Meta:
        select_on_save = True


class PrinterQuerySetManager(QuerySet):
    pass


class Printer(models.Model):
    objects = PrinterQuerySetManager.as_manager()

    firm_printer = models.CharField(verbose_name='Производитель и модель принтера', max_length=20)
    type_cart = models.CharField(verbose_name='Тип картриджа', max_length=10)
    inv_num = models.CharField(verbose_name='Инвентарный номер', max_length=15)
    date_mfd = models.DateField(verbose_name='Дата выпуска', default=date.today, blank=True)
    date_exp = models.DateField(verbose_name='Дата ввода в эксплуатацию', default=date.today, blank=True)
    owner = models.ForeignKey(WorkUser, related_name='printeritem', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firm_printer} (Инвентарный номер: {self.inv_num})"

    class Meta:
        select_on_save = True


class ScannerQuerySetManager(QuerySet):
    pass


class Scanner(models.Model):
    objects = ScannerQuerySetManager.as_manager()

    firm_scanner = models.CharField(verbose_name='Производитель и модель сканера', max_length=20)
    inv_num = models.CharField(verbose_name='Инвентарный номер', max_length=15)
    date_mfd = models.DateField(verbose_name='Дата выпуска', default=date.today, blank=True)
    date_exp = models.DateField(verbose_name='Дата ввода в эксплуатацию', default=date.today, blank=True)
    owner = models.ForeignKey(WorkUser, related_name='scanneritem', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firm_scanner} (Инвентарный номер: {self.inv_num})"

    class Meta:
        select_on_save = True
