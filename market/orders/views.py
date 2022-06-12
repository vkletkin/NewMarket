from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': Order.objects.all()})


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def orders_app(request):
    return render(request, 'main_app.html')
