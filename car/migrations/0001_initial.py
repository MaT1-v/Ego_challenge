# Generated by Django 4.2.1 on 2023-05-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=20, verbose_name="Marca")),
                ("model", models.CharField(max_length=35, verbose_name="Modelo")),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("red", "Rojo"),
                            ("blue", "Azul"),
                            ("green", "Verde"),
                            ("white", "Blanco"),
                            ("black", "Negro"),
                        ],
                        max_length=20,
                        verbose_name="Color",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("sedan", "Sedan"),
                            ("suv", "SUV"),
                            ("hatchback", "Hatchback"),
                            ("coupe", "Coupe"),
                        ],
                        max_length=30,
                        verbose_name="Categoria",
                    ),
                ),
                ("description", models.TextField(verbose_name="Descripcion")),
                ("year", models.IntegerField(verbose_name="Año")),
                ("price", models.IntegerField(verbose_name="Precio")),
                ("image", models.ImageField(upload_to="cars", verbose_name="Imagen")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creacion"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de Edicion"
                    ),
                ),
            ],
        ),
    ]
