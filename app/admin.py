from django.contrib import admin
from app.models import Topic, Entry

# Register your models here.
#Se nao colocarmos os modelos aqui entao eles nao vao aparecer no painel de admin
admin.site.register(Topic)
admin.site.register(Entry)
