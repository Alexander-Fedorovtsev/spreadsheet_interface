# Generated by Django 2.2.28 on 2022-07-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('order_number', models.IntegerField(unique=True)),
                ('cost_usd', models.FloatField()),
                ('cost_rub', models.FloatField()),
                ('delivery_date', models.DateTimeField(verbose_name='delivery date')),
            ],
        ),
    ]