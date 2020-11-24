# Generated by Django 3.1.3 on 2020-11-22 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salesscript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutationone', models.TextField()),
                ('greetingsone', models.TextField()),
                ('usernameone', models.TextField()),
                ('companynameone', models.TextField()),
                ('problemstatementone', models.TextField()),
                ('backstorytwo', models.TextField()),
                ('productnamethree', models.TextField()),
                ('qualifierquestionsthree', models.TextField()),
                ('productpresentationfour', models.TextField()),
                ('rapportquestionfive', models.TextField()),
                ('customerdoubtssix', models.TextField()),
                ('answertocustomersix', models.TextField()),
                ('productnameseven', models.TextField()),
                ('painpointseven', models.TextField()),
                ('productidealstateeight', models.TextField()),
                ('problemstatementnine', models.TextField()),
                ('productdescriptionelevan', models.TextField()),
                ('productnametwelve', models.TextField()),
                ('whatdoesitdotwelve', models.TextField()),
                ('pricetwelve', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
