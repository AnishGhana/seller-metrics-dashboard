from decimal import Decimal

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def units_sold(self):
        return sum(sale.quantity for sale in self.sales.all())

    @property
    def revenue(self):
        return sum((sale.quantity * sale.sale_price for sale in self.sales.all()), Decimal("0.00"))

    @property
    def profit(self):
        return self.revenue - (self.units_sold * self.unit_cost)

    @property
    def low_stock(self):
        return self.inventory <= self.reorder_level


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    quantity = models.PositiveIntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_on = models.DateField()

    class Meta:
        ordering = ["-sold_on", "-id"]

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
