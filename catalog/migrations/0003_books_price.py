# Generated by Django 3.2.3 on 2021-06-04 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210603_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
