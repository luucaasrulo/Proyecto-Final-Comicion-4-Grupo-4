from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {'nombre': 'Informatorio'}
    return render(request,template_name,context)

def contacto(request):
    template_name = 'contacto.html'
    nombres = ['Carlos','Ian','Lucas']
    context = {'nombres': nombres}
    return render(request,template_name,context)
def acerca(request):
    template_name = 'acercade.html'
    context = {}
    return render(request,template_name,context)