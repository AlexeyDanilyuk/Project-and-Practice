# Generated by Django 2.0 on 2020-04-10 15:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_monitor', models.CharField(max_length=20, verbose_name='Производитель и модель монитора')),
                ('diag', models.CharField(max_length=5, verbose_name='Диагональ')),
                ('inv_num', models.CharField(max_length=15, verbose_name='Инвентарный номер')),
                ('date_mfd', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата выпуска')),
                ('date_exp', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата ввода в эксплуатацию')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='monitoritem', to='userapp.WorkUser')),
            ],
            options={
                'select_on_save': True,
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_printer', models.CharField(max_length=20, verbose_name='Производитель и модель принтера')),
                ('type_cart', models.CharField(max_length=10, verbose_name='Тип картриджа')),
                ('inv_num', models.CharField(max_length=15, verbose_name='Инвентарный номер')),
                ('date_mfd', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата выпуска')),
                ('date_exp', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата ввода в эксплуатацию')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='printeritem', to='userapp.WorkUser')),
            ],
            options={
                'select_on_save': True,
            },
        ),
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_scanner', models.CharField(max_length=20, verbose_name='Производитель и модель сканера')),
                ('inv_num', models.CharField(max_length=15, verbose_name='Инвентарный номер')),
                ('date_mfd', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата выпуска')),
                ('date_exp', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата ввода в эксплуатацию')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scanneritem', to='userapp.WorkUser')),
            ],
            options={
                'select_on_save': True,
            },
        ),
        migrations.CreateModel(
            name='SysBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motherboard', models.CharField(max_length=30, verbose_name='Материнская плата')),
                ('processor', models.CharField(max_length=30, verbose_name='Процессор')),
                ('hdd', models.CharField(max_length=30, verbose_name='Жесткий диск')),
                ('ram', models.CharField(max_length=10, verbose_name='ОЗУ')),
                ('inv_num', models.CharField(max_length=15, verbose_name='Инвентарный номер')),
                ('os', models.CharField(max_length=30, verbose_name='Операционная система')),
                ('date_mfd', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата выпуска')),
                ('date_exp', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата ввода в эксплуатацию')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sysblockitem', to='userapp.WorkUser')),
            ],
            options={
                'select_on_save': True,
            },
        ),
        migrations.CreateModel(
            name='Ups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_ups', models.CharField(max_length=20, verbose_name='Производитель и модель ИБП')),
                ('power', models.CharField(max_length=5, verbose_name='Мощность (ВА)')),
                ('inv_num', models.CharField(max_length=15, verbose_name='Инвентарный номер')),
                ('date_mfd', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата выпуска')),
                ('date_exp', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата ввода в эксплуатацию')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='upsitem', to='userapp.WorkUser')),
            ],
            options={
                'select_on_save': True,
            },
        ),
    ]
