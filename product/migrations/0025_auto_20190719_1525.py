# Generated by Django 2.2.3 on 2019-07-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20190710_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='pic.jpg', upload_to='products/%y/%m/%d'),
        ),
    ]
