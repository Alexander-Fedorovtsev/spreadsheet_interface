from typing import Counter
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Orders
from .sheetdata import Gsheet2df
from django.core.paginator import Paginator
from qsstats import QuerySetStats
import datetime
from django.db.models import Sum, Max, Min


PAGES: int = 10
# Create your views here.
def index(request):
    return HttpResponse("Hello")

def index2(request):
    template = "base.html"
    orders = Orders.objects.order_by('delivery_date')
    max_order = Orders.objects.aggregate(Max("delivery_date"))["delivery_date__max"]
    min_order = Orders.objects.aggregate(Min("delivery_date"))["delivery_date__min"]
    sum_order = Orders.objects.values("delivery_date").annotate(sum_cost_usd=Sum("cost_usd")).order_by('delivery_date')
    sum_cost = Orders.objects.aggregate(Sum("cost_usd"))["cost_usd__sum"]
    paginator = Paginator(orders, PAGES)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    valu=[]
    for value in sum_order:
        valu.append([value["delivery_date"],value["sum_cost_usd"]])
    context = {
        "page_obj": page_obj,
        'values': valu,
        "max_order": max_order,
        "min_order": min_order,
        "sum_order": sum_order,
        "sum_cost": sum_cost,
    }
    return render(request, template, context)

def update_bd(request):
    df = Gsheet2df("Kanal_test").getsheet()
    template = "base.html"
    
    context = {
        "page_obj": df,
    
    }
    return render(request, template, context)