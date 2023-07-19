# Generated by Django 4.2.3 on 2023-07-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=32)),
                ('payment_method', models.CharField(max_length=32)),
                ('payment_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
