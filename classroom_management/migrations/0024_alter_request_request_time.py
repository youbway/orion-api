# Generated by Django 3.2.12 on 2022-05-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0023_auto_20220524_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
