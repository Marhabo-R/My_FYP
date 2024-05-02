from core.models import Product, Category, Vendor
from django import forms

from userauths.models import User


# from bootstrap_datepicker_plus import DatePickerInput


class AddProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Product Title", "class":"form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Product Description", "class":"form-control", "rows": 5}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Sale Price", "class":"form-control"}))
    old_price = forms.CharField(required=False, widget=forms.NumberInput(attrs={'placeholder': "Old Price", "class":"form-control"}))
    type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Type of product e.g organic cream", "class":"form-control"}))
    stock_count = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "How many are in stock?", "class":"form-control"}))
    life = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "How long would this product live?", "class":"form-control"}))
    mfd = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': "e.g: 22-11-02", "class":"form-control"}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Tags", "class":"form-control"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category",
                                      widget=forms.Select(attrs={"class": "form-control"}))
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), empty_label="Select Vendor",
                                    widget=forms.Select(attrs={"class": "form-control"}))
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select User",
                                    widget=forms.Select(attrs={"class": "form-control"}))
    # unit = forms.ChoiceField(choices=Product.UNIT_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    # product_status = forms.ChoiceField(choices=Product.STATUS, widget=forms.Select(attrs={"class": "form-control"}))
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    in_stock = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    featured = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    digital = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    specifications = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Product Specifications", "class": "form-control", "rows": 5}))

    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'old_price',
            'type',
            'stock_count',
            'life',
            'mfd',
            'tags',
            'digital',
            'category',
            'vendor',
            'user',
            'unit',
            'product_status',
            'status',
            'in_stock',
            'featured',
            'specifications',
        ]