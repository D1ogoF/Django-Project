from django.shortcuts import render
from .models import Topic 
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """Pagina principal."""
    return render(request, 'app/index.html')#o Django procura diretamente por uma pasta chamada template o app no caminho que passamos se refere au app dentro da pasta templates


def topics(request):
    """Mostra todos os assuntos."""
    topic = Topic.objects.order_by('date_added')#Por default esta a organizar do mais antigo au mais rececente
    context = {'topics':topic}
    return render(request, 'app/topics.html', context)


def topic(request, topic_id):
    """Mostra um unico assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'app/topic.html', context)


def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nehum dado submetido, cria um formulario em branco.
        form = TopicForm()
    else:
        # Dados de POST submetidos, processa os dados.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save() # Salva os dados no banco de dados.
            return HttpResponseRedirect(reverse('topics'))

    context = {'form':form}
    return render(request, 'app/new_topic.html', context)