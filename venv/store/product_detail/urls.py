from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.new_product_detail),
]