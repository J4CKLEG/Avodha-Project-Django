from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from .forms import ContactForm
from .models import Category, Product

# Create your views here.

def home(request, c_slug=None):
    c_page = None
    prodt = None
    cat = None
    paginator = Paginator(Product.objects.filter(available=True).all(), 2)

    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        prodt = Product.objects.filter(category=c_page, available=True)
        paginator = Paginator(prodt, 2)
    else:
        cat = Category.objects.all()

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
        prod = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'item.html', {'pr': prod})

def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    return render(request, 'contact.html', {'form': form})
