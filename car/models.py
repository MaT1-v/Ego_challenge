from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.


class Car(models.Model):
    CATEGORY_CHOICES = [
        ("car", "Auto"),
        ("pickup", "Camioneta"),
        ("comecial", "Comercial"),
        ("suv", "SUV"),
        ("cross", "CrossOver"),
    ]
    COLOR_CHOICES = [
        ("red", "Rojo"),
        ("blue", "Azul"),
        ("green", "Verde"),
        ("white", "Blanco"),
        ("black", "Negro"),
    ]
    brand = models.CharField(max_length=20, verbose_name="Marca")
    model = models.CharField(max_length=35, verbose_name="Modelo")
    color = models.CharField(max_length=20, verbose_name="Color", choices=COLOR_CHOICES)
    category = models.CharField(max_length=30, verbose_name="Categoria", choices=CATEGORY_CHOICES)
    description = models.TextField(verbose_name="Descripcion")
    # hybrid = models.BooleanField(verbose_name="hibrido")
    year = models.IntegerField(verbose_name="Año")
    price = models.IntegerField(verbose_name="Precio")
    image = models.ImageField(verbose_name="Imagen", upload_to="cars", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    # def get_absolute_url(self):
    #     return reverse('car_detail', args=[str(self.id)]) + '?extra_info=true'

    class meta:
        verbose_name = "auto"
        verbose_name_plural = "autos"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.id} {self.brand} {self.model} ({self.year})"


class Extra_info(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="extra_info")
    engine = models.CharField(max_length=20, verbose_name="Motor")
    transmission = models.CharField(max_length=35, verbose_name="Transmision")
    suspension = models.CharField(max_length=20, verbose_name="Suspension")
    brakes = models.CharField(max_length=30, verbose_name="Frenos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class meta:
        verbose_name = "extra_info"
        verbose_name_plural = "extra_info"

    def __str__(self):
        return f"{self.car.brand} {self.car.model} - Extra Info"
