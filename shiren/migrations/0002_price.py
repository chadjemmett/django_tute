# Generated by Django 4.1.1 on 2022-11-19 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiren', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', models.CharField(max_length=256)),
                ('transaction', models.CharField(max_length=16)),
            ],
        ),
    ]
