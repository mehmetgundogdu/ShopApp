from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Brand, BrandModel, Comment
from .forms import CommentForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from cart.forms import CartAddProductForm
from cart.cart import Cart
# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avaiable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, avaiable=True)
    form = CommentForm(request.POST or None)
    cart_product_form = CartAddProductForm()
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.user = request.user
        comment.save()
        return redirect(request.path)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'form': form,
                   'cart_product_form': cart_product_form})

def logout_page(request):
    cart = Cart(request)
    cart.clear()
    logout(request)
    return HttpResponseRedirect('/')




