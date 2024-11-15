# Generated by Django 5.1.3 on 2024-11-13 13:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercios', '0004_comercio_contacto_comercio_direccion_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='categoria',
            field=models.CharField(choices=[('restaurante', 'Restaurante'), ('ferreteria', 'Ferretería'), ('heladeria', 'Heladería'), ('mascotas', 'Tienda de Mascotas'), ('tienda', 'Tienda de barrio'), ('farmacia', 'Farmacia'), ('hotel', 'Hotel')], max_length=50),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
