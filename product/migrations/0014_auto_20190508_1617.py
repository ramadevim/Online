# Generated by Django 2.2 on 2019-05-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20190508_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
    ]
