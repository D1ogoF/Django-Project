from django.shortcuts import render

# Create your views here.

def index(request):
    """Pagina principal"""
    return render(request, 'app/index.html')#o Django procura diretamente por uma pasta chamada template o app no caminho que passamos se refere au app dentro da pasta templates
