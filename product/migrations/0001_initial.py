# Generated by Django 2.2 on 2019-05-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField(default=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.9, max_digits=20)),
            ],
        ),
    ]
