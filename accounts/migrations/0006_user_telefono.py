# Generated by Django 4.0.6 on 2022-08-23 18:10

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.IntegerField(default='00000000', max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(8)], verbose_name='N° DNI'),
        ),
    ]
