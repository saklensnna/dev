# Generated by Django 5.1.7 on 2025-03-20 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('empcode', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.position')),
            ],
        ),
    ]
