from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Ship, HomeContent, AboutContent

# HOME (Landing page)
def landing_home(request):
    if not request.user.is_authenticated:
        return redirect('login')   # ✅ better redirect

    home_data = HomeContent.objects.all()   # ✅ fixed indentation
    return render(request, 'landing_home.html', {'home_data': home_data})


# SHIPS PAGE
def ships(request):
    if not request.user.is_authenticated:
        return redirect('login')

    ships = Ship.objects.all()
    return render(request, "ships.html", {"ships": ships})


# ABOUT PAGE
def about(request):
    if not request.user.is_authenticated:
        return redirect('login')   # ✅ keep consistent

    about_data = AboutContent.objects.first()
    return render(request, 'about.html', {'about_data': about_data})


# Ship Detail
def ship_detail(request, ship_id):
    if not request.user.is_authenticated:
        return redirect('login')

    ship = get_object_or_404(Ship, id=ship_id)
    return render(request, "ship_detail.html", {"ship": ship})

# REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created! Please login.")
        return redirect('login')

    return render(request, "register.html")


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ships') 
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "login.html")


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')