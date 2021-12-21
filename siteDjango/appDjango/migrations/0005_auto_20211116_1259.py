# Generated by Django 3.2.9 on 2021-11-16 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0004_auto_20211116_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='Worker_Login',
            field=models.CharField(default='some string', max_length=25),
        ),
        migrations.AddField(
            model_name='provider',
            name='Worker_Password',
            field=models.CharField(default='some string', max_length=25),
        ),
        migrations.AddField(
            model_name='storemanager',
            name='Worker_Login',
            field=models.CharField(default='some string', max_length=25),
        ),
        migrations.AddField(
            model_name='storemanager',
            name='Worker_Password',
            field=models.CharField(default='some string', max_length=25),
        ),
        migrations.AlterField(
            model_name='anons',
            name='Anons_DateManaProducts',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 7, 59, 17, 589785, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditureinvoice',
            name='Expend_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 7, 59, 17, 593689, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Expiration_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 7, 59, 17, 591737, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Production_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 7, 59, 17, 591737, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='receiptinvoice',
            name='Receipt_Date',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 7, 59, 17, 590785, tzinfo=utc)),
        ),
    ]