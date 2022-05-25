# Generated by Django 3.2.12 on 2022-05-23 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_management', '0009_alter_session_sessionsubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='SessionLead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Staffs', to='classroom_management.staff'),
        ),
        migrations.AlterField(
            model_name='session',
            name='SessionSubject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SessionSubjects', to='classroom_management.subject'),
        ),
        migrations.AlterField(
            model_name='session',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SessionClassrooms', to='classroom_management.classroom'),
        ),
    ]
