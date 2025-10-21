from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'restaurantapp/index.html')
def menu(request):
    return render(request, 'restaurantapp/menu.html')   
def admin(request):
    return render(request, 'restaurantapp/admin.html')
def contact(request):
    return render(request, 'restaurantapp/contact.html')
def report(request):
    return render(request, 'restaurantapp/report.html')