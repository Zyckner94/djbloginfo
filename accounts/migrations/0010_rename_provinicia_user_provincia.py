# Generated by Django 4.0.6 on 2022-08-24 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_domicilio_user_provinicia_alter_user_dni_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='provinicia',
            new_name='provincia',
        ),
    ]
