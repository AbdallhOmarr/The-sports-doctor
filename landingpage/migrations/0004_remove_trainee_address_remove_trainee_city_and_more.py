# Generated by Django 4.0.4 on 2023-03-24 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_remove_trainer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='city',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='height',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='weight',
        ),
    ]