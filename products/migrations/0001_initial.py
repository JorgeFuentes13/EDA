# Generated by Django 4.2.7 on 2023-12-05 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('destacado', models.BooleanField(default=False)),
                ('image1', models.CharField(default='-', max_length=200)),
                ('clasificacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.clasificion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Atributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_atributo', models.CharField(max_length=200)),
                ('atributo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.atributo')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producto')),
            ],
        ),
    ]