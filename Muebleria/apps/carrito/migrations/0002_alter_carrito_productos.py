# Generated by Django 4.2.4 on 2023-08-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_venta_masiva_remove_producto_categoria_and_more'),
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(to='producto.producto_venta_masiva'),
        ),
    ]