# Generated by Django 5.0.6 on 2024-10-08 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_remove_pedido_produto_pedido_produto"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoria",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]