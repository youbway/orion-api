# Generated by Django 3.2.12 on 2022-05-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0003_auto_20220522_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='role_id',
            new_name='role',
        ),
    ]
