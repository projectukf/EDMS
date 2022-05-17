# Generated by Django 4.0.3 on 2022-05-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(max_length=120),
        ),
    ]
