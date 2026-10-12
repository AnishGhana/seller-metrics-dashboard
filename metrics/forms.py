from django import forms
from django.utils import timezone

from .models import Product, Sale


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "unit_price", "unit_cost", "inventory", "reorder_level"]
        widgets = {
            "unit_price": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "unit_cost": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "inventory": forms.NumberInput(attrs={"min": "0"}),
            "reorder_level": forms.NumberInput(attrs={"min": "0"}),
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["product", "quantity", "sale_price", "sold_on"]
        widgets = {
            "quantity": forms.NumberInput(attrs={"min": "1"}),
            "sale_price": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "sold_on": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sold_on"].initial = timezone.localdate()

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get("product")
        quantity = cleaned_data.get("quantity")
        if product and quantity and quantity > product.inventory:
            self.add_error("quantity", f"Only {product.inventory} units of {product.name} are in inventory.")
        return cleaned_data
