# Generated by Django 3.1.3 on 2020-11-22 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesscripts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesscript',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 22, 15, 1, 17, 655293)),
        ),
        migrations.AddField(
            model_name='salesscript',
            name='scripttitle',
            field=models.CharField(default='some string', max_length=250),
        ),
    ]
