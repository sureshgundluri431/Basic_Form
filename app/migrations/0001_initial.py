# Generated by Django 5.1 on 2024-10-07 01:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Details',
            fields=[
                ('Customer_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Customer_Name', models.CharField(max_length=40)),
                ('Customer_Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_Details',
            fields=[
                ('Product_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=200)),
                ('Customer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer_details')),
            ],
        ),
    ]
