from django.dispatch import receiver
from django.db import models
import random
import string
from django.utils.text import slugify
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
from hitcount.views import HitCountDetailView
from .models import Item
from .forms import ItemForm

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


class ItemDetailView(HitCountDetailView):
    model = Item
    template_name = "product.html"
    # context_object_name = 'object'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            'popular_posts': Item.objects.order_by('-hit_count_generic__hits', '-create_date')[:4],
        })
        return context


# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "product.html"


def products(request):
    context = {'items': Item.objects.all()}
    return render(request, "products.html", context)


@login_required(login_url="account_login")
def ItemCreate(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Not authorized to write a post')
        return redirect('core:homepage')

    else:
        if request.method == "POST":
            form = ItemForm(request.POST, request.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                item.createDate = timezone.now()
                item.slug = unique_slug_generator(item)
                item.save()
                return redirect('core:homepage')
            else:
                return render(request, "item_form.html", {'form': form})
        else:
            form = ItemForm()
            return render(request, "item_form.html", {'form': form})


# ============== Slug Generator ==============

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.slug_title.lower())

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# ============== End of Slug Generator ==============


@login_required(login_url='account_login')
def ItemModify(request, slug):
    item = get_object_or_404(Item, slug=slug)
    if not request.user.is_superuser:
        messages.warning(request, 'Not authorized to modify the post')
        return redirect('core:homepage')
    else:
        if request.method == "GET":
            form = ItemForm(instance=item)
            context = {'item': item, 'form': form}
            return render(request, 'item_form.html', context)
        else:
            form = ItemForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                item = form.save(commit=False)
                item.slug = unique_slug_generator(item)
                item.modifyDate = timezone.now()
                item.save()
                return redirect('core:product', slug=item.slug)
            else:
                context = {'item': item, 'form': form}
                return render(request, 'item_form.html', context)


@login_required(login_url='account_login')
def ItemDelete(request, slug):
    item = get_object_or_404(Item, slug=slug)
    if not request.user.is_superuser:
        messages.warning(request, 'Not authorized to delete the post')
    else:
        item.delete()
        messages.info(request, 'Successfully deleted your post.')
    return redirect('core:homepage')
