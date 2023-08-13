# Generated by Django 4.2.4 on 2023-08-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_venta_masiva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(max_length=100)),
                ('dimensiones', models.CharField(max_length=100)),
                ('disponibilidad', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='modificado')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='sub_categoria',
        ),
    ]
