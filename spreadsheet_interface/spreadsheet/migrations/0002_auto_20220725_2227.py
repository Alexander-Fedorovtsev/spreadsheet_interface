# Generated by Django 2.2.28 on 2022-07-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
    ]
