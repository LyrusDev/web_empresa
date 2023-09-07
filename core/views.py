from django.shortcuts import render

# Create your views here.
# Inicio = home/
def home(request):
    return render(request, 'core/home.html')

# Historia = about/
def about(request):
    return render(request, 'core/about.html')

# Visitanos = store/
def store(request):
    return render(request, 'core/store.html')
