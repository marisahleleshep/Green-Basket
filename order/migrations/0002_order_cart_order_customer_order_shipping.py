# Generated by Django 4.2.3 on 2023-07-15 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
        ('cart', '0002_shopping_cart_products'),
        ('customer', '0002_customer_user'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.shopping_cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping.shipping'),
        ),
    ]
