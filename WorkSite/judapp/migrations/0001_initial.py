# Generated by Django 2.0 on 2020-04-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JudSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jud_site', models.CharField(max_length=150, verbose_name='Полное наименование СУ')),
                ('jud_site_short', models.CharField(max_length=25, verbose_name='Сокращенное наименование СУ')),
            ],
            options={
                'ordering': ('jud_site_short',),
                'select_on_save': True,
            },
        ),
    ]
