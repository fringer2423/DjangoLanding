from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard


def index(request):
    slider_list = CmsSlider.objects.all()
    card_1 = PriceCard.objects.get(pk=1)
    card_2 = PriceCard.objects.get(pk=2)
    card_3 = PriceCard.objects.get(pk=3)
    table_list = PriceTable.objects.all()
    form = OrderForm()
    content = {'slider_list': slider_list,
               'card_1': card_1,
               'card_2': card_2,
               'card_3': card_3,
               'table_list': table_list,
               'form': form}
    return render(request, 'index.html', content)


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    some_order = Order(order_name=name, order_phone=phone)
    some_order.save()
    return render(request, 'thanks.html')
