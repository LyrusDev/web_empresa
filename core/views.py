from django.shortcuts import render

# Create your views here.
# Inicio = home/
def home(request):
    return render(request, 'core/home.html')

# Historia = about/
def about(request):
    return render(request, 'core/about.html')
 
# Servicios = services/
def services(request):
    return render(request, 'core/services.html')

# Visitanos = store/
def store(request):
    return render(request, 'core/store.html')

# Contacto = contact/
def contact(request):
    return render(request, 'core/contact.html')

# Blog = blog/
def blog(request):
    return render(request, 'core/blog.html')

# Sample = sample/
def sample(request):
    return render(request, 'core/sample.html')