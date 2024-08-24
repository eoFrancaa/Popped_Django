# Generated by Django 5.0.6 on 2024-08-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_produto"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=100, null=True)),
                ("password", models.CharField(max_length=30, null=True)),
            ],
        ),
    ]