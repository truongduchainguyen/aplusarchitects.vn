# Generated by Django 2.2.3 on 2020-04-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190802_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Featured'),
        ),
    ]
