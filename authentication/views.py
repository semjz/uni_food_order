from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUPForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def sign_up(request):
    if request.method == 'POST':
        form = SignUPForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            login(request, user)
            return redirect('order_food:welcome')
    else:
        form = SignUPForm()
    return render(request, 'registration/sign_up.html', {'form': form})


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    next_page = reverse_lazy("order_food:welcome")




