# Generated by Django 3.1.1 on 2020-09-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200909_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposition',
            name='no_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='proposition',
            name='yes_count',
            field=models.IntegerField(default=0),
        ),
    ]
