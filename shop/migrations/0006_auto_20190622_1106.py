# Generated by Django 2.2.2 on 2019-06-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190622_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
