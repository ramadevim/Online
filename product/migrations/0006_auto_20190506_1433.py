# Generated by Django 2.2 on 2019-05-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_feautured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='feautured',
            new_name='featured',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=True, max_length=200),
        ),
    ]
