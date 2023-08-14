from django import forms
from .models import Shopping_cart

class ShoppingCartForm(forms.ModelForm):
    class Meta:
        model = Shopping_cart
        fields = "__all__"

