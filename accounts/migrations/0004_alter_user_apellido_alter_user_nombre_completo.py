# Generated by Django 4.0.6 on 2022-08-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_telefono_user_apellido_user_dni_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombre_completo',
            field=models.CharField(max_length=20),
        ),
    ]