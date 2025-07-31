from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'count', 'description', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Mahsulot nomini kiriting",
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': "0",
                'required': True
            }),
            'count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "0",
                'min': "0"
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Mahsulot haqida batafsil ma'lumot"
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
        }

