# Generated by Django 2.0.3 on 2018-03-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0008_auto_20180315_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='Appointment_no',
            field=models.CharField(default=0, max_length=250),
        ),
    ]
