# Generated by Django 4.2.11 on 2024-09-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kombuchacalendar', '0003_alter_batch_options_batch_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='sweetener',
            field=models.CharField(choices=[('h', 'Honey'), ('s', 'Sugar')], default='s', max_length=1),
        ),
        migrations.AddField(
            model_name='batch',
            name='tea_flavor',
            field=models.CharField(choices=[('bl', 'Black Tea'), ('pg', 'Pear Ginger Black Tea'), ('bb', 'Blueberry Black Tea'), ('jg', 'Jasmine Green Tea'), ('sg', 'Strawberry Green Tea'), ('cg', 'Coconut Green Tea')], default='bl', max_length=2),
        ),
    ]
