import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ego.settings")
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Car
from .serializers import CarSerializer



@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def car_data():
    return {
        "brand": "Toyota",
        "model": "Corolla",
        "color": "Red",
        "category": "Sedan",
        "description": "A reliable car for everyday use",
        "year": 2018,
        "price": 15000.0,
        "image": "https://example.com/toyota-corolla.jpg",
    }

@pytest.fixture
def car(api_client, car_data):
    response = api_client.post(reverse("car-list"), car_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    return Car.objects.get(pk=response.data["id"])


def test_list_cars(api_client, car):
    response = api_client.get(reverse("car-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == car.id

def test_filter_cars_by_price(api_client, car):
    response = api_client.get(reverse("car-list"), {"filter": "price", "order": "asc"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == car.id

def test_filter_cars_by_year(api_client, car):
    response = api_client.get(reverse("car-list"), {"filter": "year", "order": "asc"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == car.id

def test_filter_cars_by_category(api_client, car):
    response = api_client.get(reverse("car-list"), {"category": "Sedan"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == car.id

def test_create_car(api_client, car_data):
    response = api_client.post(reverse("car-list"), car_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Car.objects.count() == 1
    assert Car.objects.get().brand == "Toyota"

def test_retrieve_car(api_client, car):
    response = api_client.get(reverse("car-detail", args=[car.id]))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == car.id

def test_update_car(api_client, car):
    data = {"brand": "Honda"}
    response = api_client.put(reverse("car-detail", args=[car.id]), data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert Car.objects.get().brand == "Honda"

def test_delete_car(api_client, car):
    response = api_client.delete(reverse("car-detail", args=[car.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Car.objects.count() == 0