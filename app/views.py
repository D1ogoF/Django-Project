from django.shortcuts import render
from .models import Topic 

# Create your views here.

def index(request):
    """Pagina principal"""
    return render(request, 'app/index.html')#o Django procura diretamente por uma pasta chamada template o app no caminho que passamos se refere au app dentro da pasta templates


def topics(request):
    """Mostra todos os assuntos"""
    topic = Topic.objects.order_by('date_added')
    context = {'topics':topic}
    return render(request, 'app/topics.html', context)