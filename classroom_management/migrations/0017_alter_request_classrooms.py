# Generated by Django 3.2.12 on 2022-05-23 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0016_auto_20220523_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='Classrooms',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='RequestClassroom', to='classroom_management.classroom'),
        ),
    ]
