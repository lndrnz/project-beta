# Generated by Django 4.0.3 on 2022-08-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0003_alter_serviceappointment_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceappointment',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
