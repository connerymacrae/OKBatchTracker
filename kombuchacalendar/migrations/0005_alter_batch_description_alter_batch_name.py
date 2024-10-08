# Generated by Django 4.2.11 on 2024-09-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kombuchacalendar', '0004_batch_sweetener_batch_tea_flavor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='description',
            field=models.TextField(help_text='Batch Size, SCOBY Origin, etc. '),
        ),
        migrations.AlterField(
            model_name='batch',
            name='name',
            field=models.CharField(help_text='Give your batch a name if you want...', max_length=50),
        ),
    ]
