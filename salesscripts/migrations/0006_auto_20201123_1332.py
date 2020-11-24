# Generated by Django 3.1.3 on 2020-11-23 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesscripts', '0005_auto_20201123_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesscript',
            name='answertocustomersix',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='backstorytwo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='companynameone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='customerdoubtssix',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='greetingsone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='painpointseven',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='pricetwelve',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='problemstatementnine',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='problemstatementone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='productdescriptionelevan',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='productidealstateeight',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='productnameseven',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='productnamethree',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='productnametwelve',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='productpresentationfour',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 13, 32, 49, 814823)),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='qualifierquestionsthree',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='rapportquestionfive',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='salutationone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='scripttitle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='usernameone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesscript',
            name='whatdoesitdotwelve',
            field=models.TextField(blank=True),
        ),
    ]