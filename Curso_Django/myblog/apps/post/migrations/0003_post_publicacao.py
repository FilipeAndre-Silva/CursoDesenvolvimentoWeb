# Generated by Django 3.1 on 2020-08-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200821_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publicacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]