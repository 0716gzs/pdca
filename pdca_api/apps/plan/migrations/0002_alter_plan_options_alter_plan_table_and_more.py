# Generated by Django 4.2.15 on 2024-08-31 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': '计划困难等级表', 'verbose_name_plural': '计划困难等级表'},
        ),
        migrations.AlterModelTable(
            name='plan',
            table='plan',
        ),
        migrations.AlterModelTable(
            name='planlevel',
            table='plan_level',
        ),
    ]
