# Generated by Django 4.0.4 on 2023-03-18 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='username',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='username',
        ),
    ]
