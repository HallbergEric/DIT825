# Generated by Django 3.2.9 on 2021-12-27 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_alter_aimodel_testbutton'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aimodel',
            name='testbutton',
        ),
    ]
