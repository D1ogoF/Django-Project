from django.db import models

#Use to control/modif the database

class Topic(models.Model):
    """Um assunto sobre o qual o usuario esta a aprender."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) #DateTime recebe uma data e as horas, auto_now_add = True esta a dizer para ele pegar automaticamnete a data e hora do sys

    def __str__(self):
        """Devolve uma representacao em String do modelo."""
        #Usamos para no painel admin ser mais organizado e visivel
        return self.text                               
    
class Entry(models.Model):
    """Algo especifico aprendido sobre um assunto."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()#usamos TextField pois tem uma capacidade maior
    date_added = models.DateTimeField(auto_now_add=True)

    #A Meta class ela e usada para descrever aspetos do nosso model por exemplo posso escolher o nome da minha tab,dizer como escrever no plural etc
    class Meta:#Nao obrigatoria, so msm para ficar mais profissional
        verbose_name_plural = 'entries' #Faz que quando o Django querer usar Entry no plural em vez de escrever Entrys que esta mal escreve entries

    def __str__(self):
         """Devolve uma representacao em String do modelo."""
         #Retourna ate os 50 primeiros caracteres
         return self.text[:50] + '...'

