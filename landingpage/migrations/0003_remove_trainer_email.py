# Generated by Django 4.0.4 on 2023-03-18 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_remove_trainee_email_remove_trainee_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='email',
        ),
    ]
