# Generated by Django 3.2.9 on 2021-12-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20211217_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='accuracy',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='aimodel',
            name='loss',
            field=models.FloatField(default=0.0),
        ),
    ]
