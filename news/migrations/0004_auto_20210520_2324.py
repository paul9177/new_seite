# Generated by Django 3.0.3 on 2021-05-20 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210520_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='tab_10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.BigIntegerField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='meldung',
            name='text',
            field=models.TextField(verbose_name='Meldungstext'),
        ),
    ]
