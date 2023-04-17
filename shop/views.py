from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.forms import UserCreationForm
from cart.views import cart
from django.contrib import messages


# Create your views here.
def home(request, c_slug=None):
    c_page = None
    prodt = None
    cat = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)

    else:
        prodt = products.objects.filter(available=True).all()
        cat = categ.objects.all()
        paginator = Paginator(prodt, 2)

    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'pr': prodt, 'ct': cat, 'pg': pro})


def prodDetails(request, c_slug, product_slug):
    try:
        prod = products.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'item.html', {'pr': prod})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))

    return render(request, 'search.html', {'qr': query, 'pr': prod})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
