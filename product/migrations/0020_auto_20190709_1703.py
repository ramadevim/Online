# Generated by Django 2.2.2 on 2019-07-09 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20190708_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',)},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
