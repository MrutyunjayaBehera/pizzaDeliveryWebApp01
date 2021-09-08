from pizzaApp.models import CustomerModel, OrderModel, PizzaModel
from django.contrib import messages
from django.contrib.auth.models import User # inbuilt user database by django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
import emoji
import requests


# Create your views here.
def adminloginview(request):
    return render(request, 'pizzaApp/adminlogin.html')


# whatever user enters in the form we need to store those info
def authenticateadmin(request):
    username = request.POST['username']  # got the username
    password = request.POST['password']  # got the password

    user = authenticate(username=username, password=password)

    # user exist
    if user is not None and user.username == 'admin':
        login(request, user)  # after log in redirect it to the url which will call the func which will render the main page
        return redirect('adminhomepage')

    # user does not exist
    if user is None:
        messages.add_message(request, messages.ERROR, 'Invalid Credentials')
        return redirect('adminloginpage')


# now if user exists, after logging in it should go to main view page
def adminhomepageview(request):
    # after saving pizza as entered by user, we need to display it here
    context = {'pizzas': PizzaModel.objects.all()}
    return render(request, 'pizzaApp/adminhomepage.html', context)


def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')


def addpizza(request):
    # write code to add pizza(name, price) to database [watch the placeholder in adminhomepage]
    # we will use POST method to send data to server
    name = request.POST['pizza'] # pizza is the value of 'name' field of the input  
    price = request.POST['price']

    # now save the name, price entered by the user in the adminhomepage to the pizza model in database
    # name & price in orange color are the attributes of pizzaModel
    # & name, pizza in green color are the values we got from user
    PizzaModel(name=name, price=price).save()
    # now link the 'add' button to this function, but  there is no direct way, so we will go through url
    # link this function and that form (add pizza) to the same url
    return redirect('adminhomepage')  # enter the name field value of the url for redirecting


def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')


def homepageview(request):
    return render(request, 'pizzaApp/homepage.html')


def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phone no.']

    # if user already exists
    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR, 'User Already Registered')
        return redirect('homepage')

    # if user does not exists then create an user
    User.objects.create_user(username=username, password=password).save()
    # but no database to save phone number, so lets create a model for that
    lastobject = len(User.objects.all()) - 1
    CustomerModel(userid=User.objects.all()[int(lastobject)].id, phoneno=phoneno).save()
    # create a message
    messages.add_message(request, messages.ERROR, 'User Registered Successfully') 
    # now redirect user to homepage again and then customer needs to login
    return redirect('homepage')


def userloginview(request):
    return render(request, 'pizzaApp/userlogin.html')


def userauthenticate(request):
    # same as we did in user signup call
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('customerpage')
    if user is None:
        messages.add_message(request, messages.ERROR, 'Invalid Credentials')
        return redirect('userloginpage')
    # link the submitt button of login page to this function vis url

def customerwelcomeview(request):

    # user just cannot access any webpage by entering url, he/she needs to be authenticated
    if request.user.is_authenticated == False:
        return redirect('userloginpage')

    username = request.user.username
    context = {'username': username, 'pizzas': PizzaModel.objects.all()}
    return render(request, 'pizzaApp/customerwelcome.html', context)


def userlogoutview(request):
    logout(request)
    return redirect('userloginpage')

def placeorder(request):
    if request.user.is_authenticated == False:
        return redirect('userloginpage')
    
    username = request.user.username
    phoneno = CustomerModel.objects.all()[0].phoneno
    address = request.POST['address']
    ordereditems = " "
    
    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price
        
        quantity = request.POST.get(str(pizzaid), " ")
        
        if str(quantity) != "0" and str(quantity) != "":
            ordereditems = ordereditems + quantity + " " + name + " " + "for Rs." + str(int(quantity)*int(price)) + " & "
    
    # adding uer inputs to ordermodel in db and saving it
    OrderModel(username = username, phoneno = phoneno, address = address, ordereditems = ordereditems).save()
    messages.add_message(request, messages.ERROR, 'Order placed Successfully')
    return redirect('customerpage')

def userorders(request):
    orders = OrderModel.objects.filter(username=request.user.username)
    context = { 'orders': orders }
    return render(request, 'pizzaApp/userorders.html', context)

def adminorders(request):
    orders = OrderModel.objects.all()
    context = {'orders': orders}
    return render(request, 'pizzaApp/adminorders.html', context)

def acceptorder(request, orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status = "Accepted" 
    order.save()
    return redirect(request.META['HTTP_REFERER'])

def declineorder(request, orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "Declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])


