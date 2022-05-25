# Generated by Django 3.2.12 on 2022-05-23 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0017_alter_request_classrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Subjects',
            field=models.ManyToManyField(blank=True, default=None, related_name='StaffSubjects', to='classroom_management.Subject'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StaffRoles', to='classroom_management.role'),
        ),
    ]
