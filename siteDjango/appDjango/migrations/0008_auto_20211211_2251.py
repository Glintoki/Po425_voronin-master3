# Generated by Django 3.2.9 on 2021-12-11 17:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0007_auto_20211124_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Order_Name_Product',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='receiptinvoice',
            name='Receipt_Date',
            field=models.DateField(default=datetime.datetime(2021, 12, 11, 17, 51, 45, 32388, tzinfo=utc)),
        ),
    ]