# Generated by Django 3.2.4 on 2021-06-29 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passowrd',
        ),
    ]