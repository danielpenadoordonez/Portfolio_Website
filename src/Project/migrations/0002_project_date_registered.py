# Generated by Django 4.0.5 on 2022-06-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_Registered',
            field=models.DateField(auto_now=True),
        ),
    ]
