# Generated by Django 5.1.3 on 2024-11-14 00:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_tutor', '0002_rename_subjects_student_password'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects_needed', models.TextField(help_text='Subjects you need help with')),
                ('subjects_can_teach', models.TextField(help_text='Subjects you can teach')),
                ('contact_info', models.CharField(help_text='Your contact information', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]