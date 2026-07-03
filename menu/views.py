from django.shortcuts import render,redirect
from .forms import ReservationForm
from django.contrib.auth import authenticate, login




# Create your views here.

from .models import Dish

def home(request):
    return render(request, "menu/home.html")

def menu_page(request):
    dishes = Dish.objects.all()
    return render(request, "menu/menu.html", {"dishes": dishes})


def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, "menu/reservation.html", {"form": form})




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Replace with your home URL name
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "menu/login.html")

from django.shortcuts import render, redirect
from .models import Order

def place_order(request):
    if request.method == "POST":
        Order.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            plan=request.POST.get("plan"),
            address=request.POST.get("address")
        )

        return redirect("success")  # या same page

    return render(request, "index.html")
