# Generated by Django 3.2.12 on 2022-05-25 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0031_rename_rolename_role_rolename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='RolePermission',
            new_name='permission',
        ),
    ]
