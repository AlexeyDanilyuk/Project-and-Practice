from django.db import models


class Currency(models.Model):
    curr_name = models.CharField(verbose_name='Название валюты', max_length=50)
    curr_num_code = models.PositiveSmallIntegerField(verbose_name='Код валюты')
    curr_char_code = models.CharField(verbose_name='Знак валюты', max_length=3)

    def __str__(self):
        return f'{self.curr_name} ({self.curr_char_code})'


class Regions(models.Model):
    region_name = models.CharField(verbose_name='Название региона (страны)', max_length=50)
    region_code = models.CharField(verbose_name='Код региона (страны)', max_length=3)

    def __str__(self):
        return f'{self.region_name} ({self.region_code})'


class Account(models.Model):
    email = models.CharField(verbose_name='Электронная почта', max_length=50)
    mobN = models.CharField(verbose_name='Номер телефона', null=True, max_length=11)
    passwd = models.CharField(max_length=128)
    agent = models.CharField(verbose_name='Название компании', max_length=10)
    uuid_code = models.UUIDField
    region = models.ForeignKey(Regions, on_delete=models.SET_NULL, null=True, verbose_name='Страна')
    contract = models.CharField(verbose_name='Номер договора с агентом', max_length=10, default=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, verbose_name='Валюта')
    created_at = models.DateTimeField(auto_now=True)
    modify_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.mobN} ({self.email})'


class TransactionsDetail(models.Model):
    trust = models.IntegerField(verbose_name='Размер кредита доверия', null=True)
    limittransaction = models.IntegerField(verbose_name='Размер лимита списания денежных средств', null=True)
    limitperday = models.IntegerField(verbose_name='Лимит списания денег за сутки', null=True)
    modify_author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modify_at = models.DateTimeField(auto_now_add=True)


class AccountDetail(models.Model):
    uuid_code = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(verbose_name='Статус', default=True)
    type_account = models.CharField(verbose_name='Тип', max_length=50)
    tag = models.CharField(verbose_name='Комментарий', max_length=50)
    trans_detail = models.ForeignKey(TransactionsDetail, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modify_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.uuid_code} ({self.email})'
