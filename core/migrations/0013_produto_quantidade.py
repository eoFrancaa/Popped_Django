# Generated by Django 5.0.6 on 2024-10-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_categoria_capa"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="quantidade",
            field=models.IntegerField(default=0),
        ),
    ]
