from django.urls import path

from apps.views import IndexView, ProductCreateView, ProductUpdateView, ProductDetailView, ProductDeleteView, \
    MarkOutOfStockView, ArchivedProduct, ArchivedProductListView

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('archived-products/', ArchivedProductListView.as_view(), name='archived-products-page'),
    path('create/', ProductCreateView.as_view(), name='create-page'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='product-detail-page'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete-page'),
    path('products/<int:pk>/mark-out-of-stock/', MarkOutOfStockView.as_view(), name='mark-out-of-stock'),
    path('products/<int:pk>/archive-product/', ArchivedProduct.as_view(), name='archive-product'),
]


