# Generated by Django 4.0.4 on 2022-05-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataModel', '0011_originaldata_ph_originaldata_所属城市_originaldata_所属水系_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentItemsetsWithData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('itemsets', models.CharField(default='', max_length=256)),
                ('support', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='FrequentItemsetsWithStandard',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('itemsets', models.CharField(default='', max_length=256)),
                ('support', models.CharField(default='', max_length=256)),
            ],
        ),
    ]
