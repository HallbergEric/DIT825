# Generated by Django 3.2.9 on 2021-12-21 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_rename_datasetmodel_dataset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.FloatField(default=0.0)),
                ('reportedEPS', models.FloatField(default=0.0)),
                ('totalNonCurrentAssets', models.FloatField(default=0.0)),
                ('depreciation', models.FloatField(default=0.0)),
                ('proceedsFromRepaymentsOfShortTermDebt', models.FloatField(default=0.0)),
                ('currentAccountsPayable', models.FloatField(default=0.0)),
                ('symbol', models.CharField(max_length=30)),
                ('timestamp', models.CharField(max_length=30)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.dataset')),
            ],
        ),
    ]
