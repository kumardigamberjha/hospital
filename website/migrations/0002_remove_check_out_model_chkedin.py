# Generated by Django 4.0.1 on 2022-04-04 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check_out_model',
            name='chkedin',
        ),
    ]