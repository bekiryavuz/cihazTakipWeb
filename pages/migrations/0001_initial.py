# Generated by Django 3.1.7 on 2021-04-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cihazlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btNumarasi', models.IntegerField(max_length=15)),
                ('domainAdi', models.CharField(max_length=14)),
                ('isyeri', models.CharField(max_length=50)),
                ('cihazTuru', models.CharField(max_length=20)),
                ('markaAdi', models.CharField(max_length=50)),
                ('gelisNedeni', models.CharField(max_length=50)),
                ('yapilanIs', models.CharField(max_length=50)),
                ('gorevli', models.CharField(max_length=50)),
                ('gelisTarihi', models.DateField()),
                ('teslimTarihi', models.DateField()),
                ('cihazSahibi', models.CharField(max_length=50)),
                ('cihazDurum', models.CharField(max_length=50)),
            ],
        ),
    ]