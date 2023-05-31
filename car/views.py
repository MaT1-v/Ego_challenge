from rest_framework.response import Response
from .serializers import CarSerializer, Extra_infoSerializer
from .models import Car, Extra_info
from rest_framework import viewsets
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CarViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Success",
                examples={
                    "application/json": {
                        "id": 1,
                        "brand": "Toyota",
                        "model": "Corolla",
                        "color": "Red",
                        "category": "Sedan",
                        "description": "A reliable car for everyday use",
                        "year": 2018,
                        "price": 15000.0,
                        "image": "https://example.com/toyota-corolla.jpg",
                        "extra_info": [
                            {
                                "id": 2,
                                "engine": "V8",
                                "transmission": "Automatic",
                                "brakes": "ABS",
                                "suspension": "Comfort",
                            },
                            {
                                "id": 3,
                                "engine": "V10",
                                "transmission": "Manual",
                                "brakes": "Sport",
                                "suspension": "Sport",
                            },
                        ],
                    }
                },
            ),
            400: openapi.Response(description="Bad Request", examples={"application/json": {"error": "Bad Request"}}),
        }
    )
    def list(self, request):
        queryset = Car.objects.all()
        filtering = request.query_params.get("filter", None)
        ordering = request.query_params.get("order", None)
        category = request.query_params.get("category", None)
        if filtering == "price":
            if ordering == "asc":
                queryset = queryset.order_by("price")
            else:
                queryset = queryset.order_by("-price")
        elif filtering == "year":
            if ordering == "asc":
                queryset = queryset.order_by("year")
            else:
                queryset = queryset.order_by("-year")
        if category is not None:
            queryset = queryset.filter(Q(category__exact=category))
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="extra_info_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="ID of the extra info car to retrieve",
            ),
        ],
        responses={
            200: openapi.Response(
                description="Success",
                examples={
                    "application/json": {
                        "id": 1,
                        "brand": "Toyota",
                        "model": "Corolla",
                        "color": "Red",
                        "category": "Sedan",
                        "description": "A reliable car for everyday use",
                        "year": 2018,
                        "price": 15000.0,
                        "image": "https://example.com/toyota-corolla.jpg",
                        "extra_info": [
                            {
                                "id": 2,
                                "engine": "V8",
                                "transmission": "Automatic",
                                "brakes": "ABS",
                                "suspension": "Comfort",
                            },
                            {
                                "id": 3,
                                "engine": "V10",
                                "transmission": "Manual",
                                "brakes": "Sport",
                                "suspension": "Sport",
                            },
                        ],
                    },
                },
            ),
        },
    )
    def retrieve(self, request, pk=None):
        extra_info_id = request.query_params.get("extra_info_id")
        if extra_info_id is not None:
            car = Car.objects.get(pk=pk)
            extra_info = car.extra_info.get(id=extra_info_id)
            car_serializer = CarSerializer(car)
            extra_info_serializer = Extra_infoSerializer(extra_info)
            return Response(
                {
                    "id": car_serializer.data["id"],
                    "brand": car_serializer.data["brand"],
                    "model": car_serializer.data["model"],
                    "color": car_serializer.data["color"],
                    "category": car_serializer.data["category"],
                    "description": car_serializer.data["description"],
                    "year": car_serializer.data["year"],
                    "price": car_serializer.data["price"],
                    "image": car_serializer.data["image"],
                    "extra_info": extra_info_serializer.data,
                }
            )
        else:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return Response(serializer.data)

    def update(self, request, pk=None):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response(status=204)
