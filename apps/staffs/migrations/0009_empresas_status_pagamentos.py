# Generated by Django 4.0 on 2024-08-29 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0008_rename_valorizacao_fechamentos_variação'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('id_pagamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staffs.empresas')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staffs.person')),
            ],
        ),
    ]
