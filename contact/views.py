from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    # print('Tipo de petición:{} '.format(request.method))
    # Forms / instancia
    contactForm = ContactForm()
    if request.method == "POST":
        print("Metodo post")
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            print("Formulario valido")
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            message = request.POST.get('message','')
            
            email_contact = EmailMessage(
                "La Cafettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, message),
                "correo-prueba@inbox.mailtrap.io",
                ["aguizado@itsqmet.edu.ec"],
                reply_to=[email]
            )
        try:
            print("Enviando correo")
            email_contact.send()
            return redirect(reverse('contact')+'?ok')
        except Exception as e:
            print('Error: ', type(e).__name__)
            return redirect(reverse('contact')+'?fail')
    return render(request, 'contact/contact.html', {'contactForm':contactForm})
