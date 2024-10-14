from django.shortcuts import render, HttpResponse
# Create your views here.
menu="""
    

"""
def principal(request):
    return render(request,"yo/principal.html")

def Contactanos(request):
    return render(request,"yo/Contacto.html")