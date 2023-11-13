from django.urls import path
from .views import home, welcome, ChooseFood, OrderDetail, WalletDetail, OrdersDetail

app_name = 'order_food'

urlpatterns = [
   path("", home, name="home"),
   path("welcome/", welcome, name="welcome"),
   path("order-food/", ChooseFood.as_view(), name="order-food"),
   path("orders/<int:student_id>", OrdersDetail.as_view(), name="orders-detail"),
   path("order/<int:order_id>", OrderDetail.as_view(), name="order-detail"),
   path("wallet/<int:student_id>", WalletDetail.as_view(), name="order-detail"),
]