# Generated by Django 4.2.7 on 2023-12-05 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='atributo',
            table='Atributo',
        ),
        migrations.AlterModelTable(
            name='clasificion',
            table='Clasificacion',
        ),
        migrations.AlterModelTable(
            name='producto',
            table='Producto',
        ),
        migrations.AlterModelTable(
            name='producto_atributo',
            table='Producto_Atributo',
        ),
    ]
