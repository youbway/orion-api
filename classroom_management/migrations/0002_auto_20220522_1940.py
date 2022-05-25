# Generated by Django 3.2.12 on 2022-05-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='ActivityTypes',
        ),
        migrations.AddField(
            model_name='staff',
            name='ActivityTypes',
            field=models.ManyToManyField(default=None, related_name='ActivityType', to='classroom_management.Activity_type'),
        ),
    ]
