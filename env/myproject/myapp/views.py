from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def menu(request):
    return render(request,'menu.html')
def biriyani(request):
    return render(request,'biriyani.html')
def kuzimanthi(request):
    return render(request,'kuzimanthi.html')
def mojito(request):
    return render(request,'mojito.html')
def testimonial(request):
    return render(request,'testimonial.html')

