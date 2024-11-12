# Generated by Django 5.0.6 on 2024-10-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_cliente_capa_produto_capa"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedido",
            name="produto",
        ),
        migrations.AddField(
            model_name="pedido",
            name="produto",
            field=models.ManyToManyField(blank=True, to="core.produto"),
        ),
    ]