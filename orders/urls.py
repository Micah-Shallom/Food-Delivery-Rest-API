from django.urls import path
from . import views


urlpatterns = [
    path("orders/", views.HelloOrderView().as_view(), name="hello_order")
]