# Generated by Django 5.2 on 2025-04-14 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_type', models.CharField(max_length=100)),
                ('estimated_arrival_time', models.DateTimeField()),
                ('actual_arrival_time', models.DateTimeField(blank=True, null=True)),
                ('token_status', models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='active', max_length=20)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokens.farmer')),
            ],
        ),
    ]
