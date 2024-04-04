from django.urls import path
from . import views


urlpatterns = [
    path("order/", views.HelloOrderView().as_view(), name="hello_order")
]