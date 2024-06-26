from django import forms
from .models import Product, ProductSubCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

class ProductSubCategoryForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = ProductSubCategory
        fields = ['product', 'price', 'image', 'model', 'ram']
