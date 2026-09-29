from django import forms
from .models import Topic

#TopicForm herda da classe ModelForm que esta dentro do modulo forms
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
