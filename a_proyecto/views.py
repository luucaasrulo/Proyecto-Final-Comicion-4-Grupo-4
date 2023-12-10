from django.shortcuts import render

# def index(request):
#     template_name = 'post/listar_primeros_post.html'
#     context = {}
#     return render(request,template_name,context)

def contacto(request):
    template_name = 'contacto.html'
    context = {}
    return render(request,template_name,context)

def acerca(request):
    template_name = 'acercade.html'
    context = {}
    return render(request,template_name,context)