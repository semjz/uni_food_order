from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, ListView
from .forms import OrderForm
from .models import Food, Order, Wallet, Student
from django.http import HttpResponse
from django.db import transaction
from sms_service.utility import send_sms


def home(request):
    return render(request, "home.html")


@login_required(login_url="/login")
def welcome(request):
    return render(request, "welcome.html")


class ChooseFood(FormView):
    form_class = OrderForm
    template_name = "order_page.html"

    def form_valid(self, form):
        food_name = form.cleaned_data["foods"]
        required_quantity = form.cleaned_data["quantity"]
        selected_food = Food.objects.get(name=food_name)
        food_quantity = selected_food.quantity
        food_price = selected_food.price * required_quantity
        student = Student.objects.get(username=self.request.user.username)
        student_wallet = student.wallet
        student_wallet_amount = student_wallet.amount

        if student_wallet.amount < food_price:
            return HttpResponse(f"Wallet amount not enough", status=400)

        if required_quantity > food_quantity:
            print("test")
            return HttpResponse(f"Not enough food for quantity of {required_quantity}", status=400)

        entry = Food.objects.select_for_update().get(name=food_name)
        with transaction.atomic():
            entry.quantity = food_quantity - required_quantity
            student_wallet.amount = student_wallet_amount - food_price
            entry.save()
            student_wallet.save()
            order = Order.objects.create(student=student, total_amount=food_price)
            message = (f"Order:\n"
                       f" id:{order.id}"
                       f"\n food:{food_name} "
                       f"\n quantity:{required_quantity} "
                       f"\n was successful!")
            send_sms(message, student.phone_number)

        return redirect("order_food:order-detail", id=order.id)


class OrdersDetail(ListView):
    model = Order
    template_name = "all_orders_detail.html"
    paginate_by = 10

    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        return Order.objects.filter(student_id=student_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = self.get_queryset()
        return context


class OrderDetail(TemplateView):
    template_name = "order_detail.html"

    def get_context_data(self, **kwargs):
        order_id = self.kwargs["order_id"]
        order = Order.objects.get(id=order_id)

        context = {"order": order}
        return context


class WalletDetail(TemplateView):
    template_name = "wallet_detail.html"

    def get_context_data(self, **kwargs):
        student_id = self.kwargs["student_id"]
        wallet = Wallet.objects.get(id=student_id)

        context = {"wallet": wallet}
        return context







