# Generated by Django 3.1.7 on 2021-04-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210429_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cihazlar',
            name='gelisNedeni',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Geliş Nedeni'),
        ),
        migrations.AlterField(
            model_name='cihazlar',
            name='yapilanIs',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Yapılan İş'),
        ),
    ]
