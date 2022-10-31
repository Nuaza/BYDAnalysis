# Generated by Django 4.0.4 on 2022-05-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataModel', '0005_originaldata_六价铬_originaldata_挥发酚_originaldata_氟化物_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='originaldata',
            name='水质类别',
            field=models.CharField(default='Ⅴ类', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='BOD',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='COD',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='六价铬',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='总氮',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='总磷',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='挥发酚',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='氟化物',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='氨氮',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='氰化物',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='汞',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='溶解氧',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='石油类',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='砷',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='硒',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='硫化物',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='粪大肠菌群',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='铅',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='铜',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='锌',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='镉',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='阴离子表面活性剂',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='originaldata',
            name='高锰酸盐',
            field=models.CharField(default='0', max_length=64),
        ),
    ]
