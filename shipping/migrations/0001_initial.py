# Generated by Django 4.2.3 on 2023-07-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
