# Generated by Django 3.2.12 on 2022-05-22 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0004_rename_role_id_staff_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='ActivityTypes',
        ),
    ]
