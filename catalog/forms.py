from django.forms import ModelForm
from .models import Product, Version
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_preview', 'category', 'price', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_preview': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        name = self.cleaned_data['name']
        if name.lower() in forbidden_words:
            raise forms.ValidationError("Название товара не может включать запрещенные слова")
        return self.cleaned_data['name']


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
