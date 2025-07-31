from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView

from apps.forms import ProductForm
from apps.models import Product


class ArchivedProductMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_archived:
            raise Http404("Product not found")
        return obj


class IndexView(ListView):
    queryset = Product.objects.filter(is_archived=False)
    context_object_name = 'products'
    template_name = 'index.html'


class ArchivedProductListView(ListView):
    queryset = Product.objects.filter(is_archived=True)
    context_object_name = 'products'
    template_name = 'archived-product-list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create.html'
    success_url = reverse_lazy('index-page')


class ProductUpdateView(ArchivedProductMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit.html'
    success_url = reverse_lazy('index-page')


class ProductDetailView(ArchivedProductMixin, DetailView):
    model = Product
    template_name = 'view.html'
    context_object_name = 'product'


class ProductDeleteView(ArchivedProductMixin, DeleteView):
    model = Product
    template_name = 'delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('index-page')


class MarkOutOfStockView(View):
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.count = 0
        product.save()
        return redirect('product-detail-page', pk=pk)


class ArchivedProduct(View):
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        if product.is_archived:
            product.is_archived = False
        else:
            product.is_archived = True
        product.save()
        return redirect('index-page')


