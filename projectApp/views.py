from django.shortcuts import redirect, render

from .models import Product as prodcutModel, Purchase
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
   if request.user.is_authenticated:
    return redirect('items/products')
   else:
    return redirect('login/')
   return render(request, 'projectApp/login.html')

def login_view(request):
    if request.method == 'POST':
        username =  request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username == '':
            messages.error(request, 'Username must be filled')
            return redirect('/login')
        if password == '':
            messages.error(request, 'Password must be filled')
            return redirect('/login')
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('/items/products')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'projectApp/login.html')


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username'].lower()
        password = request.POST['password']
        passwordCon = request.POST['passwordCon']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('/signup')
        if username == '' :
            messages.error(request, 'Username must be filled')
            return redirect('/signup')
        if password == '' or passwordCon == '' :
            messages.error(request, 'Password must be filled')
            return redirect('/signup')
        if password != passwordCon:
            messages.error(request, 'Passwords do not match')
            return redirect('/signup')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, f'Account created for {username}!')
        return redirect('/login')

    return render(request, 'projectApp/signup.html')
@login_required
def products(request):
   products = prodcutModel.objects.all()
   return render(request, 'projectApp/products.html',{'products': products})

@login_required
def add(request):
   if request.method == 'POST':
        print(request.POST)
        print(request.POST)
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        if not price.isdigit():
            messages.error(request, 'Price should be a number.')
            return render(request, 'projectApp/add.html')
        prodcutModel.objects.create(name=name, description=description, price=price)
        messages.success(request, f'{name} have been added successfully!')
        redirect('item/product/add')
   return render(request, 'projectApp/add.html')



@login_required
def update(request , product_id=""):
    product = prodcutModel.objects.all()
    if  product_id != "" and type(int(product_id)) == int:
        product_id = prodcutModel.objects.get(id=int(product_id))
    if request.method == 'POST':
        print(request.POST)
        product = prodcutModel.objects.get(id=request.POST['select'])
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        if not product.price.isdigit():
            messages.error(request, 'Price should be a number.')
            return render(request, 'projectApp/update.html')
        product.save()
        messages.success(request, f'Product have been updated successfully!')

        return redirect('update')