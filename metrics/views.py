from decimal import Decimal

from django.contrib import messages
from django.db.models import F, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm, SaleForm
from .models import Product, Sale


def dashboard(request):
    products = Product.objects.prefetch_related("sales")
    total_revenue = sum((product.revenue for product in products), Decimal("0.00"))
    total_profit = sum((product.profit for product in products), Decimal("0.00"))
    total_units = sum(product.units_sold for product in products)
    low_stock_products = [product for product in products if product.low_stock]
    recent_sales = Sale.objects.select_related("product")[:5]
    return render(request, "metrics/dashboard.html", {
        "products": products,
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_units": total_units,
        "low_stock_products": low_stock_products,
        "recent_sales": recent_sales,
    })


def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product = form.save()
        messages.success(request, f"{product.name} was added to your catalog.")
        return redirect("dashboard")
    return render(request, "metrics/product_form.html", {"form": form})


def sale_create(request):
    form = SaleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        sale = form.save()
        Product.objects.filter(pk=sale.product_id).update(inventory=F("inventory") - sale.quantity)
        messages.success(request, f"Recorded sale of {sale.quantity} {sale.product.name} unit(s).")
        return redirect("dashboard")
    return render(request, "metrics/sale_form.html", {"form": form})


def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        name = product.name
        product.delete()
        messages.success(request, f"{name} and its sales history were removed.")
    return redirect("dashboard")
