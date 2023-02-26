from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    phone_objects = Phone.objects.all()
    if request.GET.get('sort') == 'name':
        phones = [phone for phone in phone_objects]
        phones.sort(key=lambda x: x.name)
    elif request.GET.get('sort') == 'min_price':
        phones = [phone for phone in phone_objects]
        phones.sort(key=lambda x: x.price, reverse=False)
    elif request.GET.get('sort') == 'max_price':
        phones = [phone for phone in phone_objects]
        phones.sort(key=lambda x: x.price, reverse=True)
    else:
        phones = [phone for phone in phone_objects]
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = [element for element in Phone.objects.filter(slug=slug)][0]
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
