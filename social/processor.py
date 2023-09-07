from .models import Social

def context(request):
    dict = {}
    listSocial = Social.objects.all()
    for social in listSocial:
        dict[social.key] = social.url  # Agregar valores al diccionario
    return dict
