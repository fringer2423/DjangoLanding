from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider


def index(request):
    slider_list = CmsSlider.objects.all()
    return render(request, 'index.html', {'slider_list': slider_list})


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    some_order = Order(order_name=name, order_phone=phone)
    some_order.save()
    return render(request, 'thanks.html')
