from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_products(request):
    """Simple View to show all products"""
    current_sort = None
    sort = None
    direction = None
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No Items Entered")
                return redirect(reverse('products'))
          
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
        current_sort = f'{sort}_{direction}'    

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sort': current_sort,
    }
    return render(request, "products/products.html", context)


def detail(request, product_id):
    """Show Products Details"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "products/detail.html", context)


@login_required
def add_product(request):
    """ To add product to website """
    if not request.user.is_superuser:
        messages.error(request, "GET OUT!")
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product was added')
            return redirect(reverse('detail', args=[product.id]))
        else:
            messages.error(request, 'Something seems to be wrong')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit Product """
    if not request.user.is_superuser:
        messages.error(request, "GET OUT!")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cake Updated!')
            return redirect(reverse('detail', args=[product.id]))
        else:
            messages.success(request, 'Woops, something went wrong')
    else:
        form = ProductForm(instance=product)

        template = 'products/edit_product.html'
        context = {
            'form': form,
            'product': product,
        }

        return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete Product """
    if not request.user.is_superuser:
        messages.error(request, "GET OUT!")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Cake removed')
    return redirect(reverse('products'))
