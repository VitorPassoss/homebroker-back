# Generated by Django 4.0 on 2024-08-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0009_empresas_status_pagamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechamentos',
            name='porcentagem',
            field=models.CharField(max_length=255),
        ),
    ]
