
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from django.views.generic import DetailView, View
from .models import Item

# Create your views here.

import random
import string

def page_not_found(request, exception):

    # 404 Page not found

    return render(request, '404.html', {})


def internal_server_error(request):

    # 500 internal server error

    return render(request, '500.html', {})




def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    sort = request.GET.get('sort', 'all')

    if sort == "diary":
        item_list = Item.objects.order_by(
            '-create_date').filter(category="Diary")
    elif sort == "career":
        item_list = Item.objects.order_by(
            '-create_date').filter(category="Career")
    elif sort == "relationship":
        item_list = Item.objects.order_by(
            '-create_date').filter(category="Relationship")
    elif sort == "travel":
        item_list = Item.objects.order_by(
            '-create_date').filter(category="Travel")
    else:
        item_list = Item.objects.order_by('-create_date')
    if kw:
        item_list = item_list.filter(
            Q(title__icontains=kw) |
            Q(label__icontains=kw) |
            Q(contents_short__icontains=kw) |
            Q(contents_long__icontains=kw)
        ).distinct()
    paginator = Paginator(item_list, 8)
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'page': page, 'kw': kw, 'sort': sort}
    return render(request, 'home.html', context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def products(request):
    context = {'items': Item.objects.all()}
    return render(request, "products.html", context)


