# Generated by Django 2.0.3 on 2018-03-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_auto_20180313_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='type1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='type2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='type3',
            field=models.IntegerField(default=0),
        ),
    ]
