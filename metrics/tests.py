from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Product, Sale


class DashboardTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Insulated Bottle", category="Accessories", unit_price=Decimal("25.00"),
            unit_cost=Decimal("9.00"), inventory=15, reorder_level=4,
        )

    def test_dashboard_calculates_product_metrics(self):
        Sale.objects.create(product=self.product, quantity=3, sale_price=Decimal("25.00"), sold_on=date.today())
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, "$75.00")
        self.assertContains(response, "$48.00")

    def test_sale_reduces_inventory(self):
        response = self.client.post(reverse("sale_create"), {
            "product": self.product.id, "quantity": 2, "sale_price": "25.00", "sold_on": date.today(),
        })
        self.assertRedirects(response, reverse("dashboard"))
        self.product.refresh_from_db()
        self.assertEqual(self.product.inventory, 13)

    def test_sale_cannot_exceed_inventory(self):
        response = self.client.post(reverse("sale_create"), {
            "product": self.product.id, "quantity": 20, "sale_price": "25.00", "sold_on": date.today(),
        })
        self.assertContains(response, "Only 15 units")
        self.assertEqual(Sale.objects.count(), 0)
