# Generated by Django 4.0.4 on 2022-05-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataModel', '0002_originaldata_溶解氧'),
    ]

    operations = [
        migrations.AddField(
            model_name='originaldata',
            name='BOD',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='originaldata',
            name='COD',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='originaldata',
            name='高锰酸盐',
            field=models.CharField(default='', max_length=64),
        ),
    ]
