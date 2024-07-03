from django.contrib import admin # type: ignore
from .models import Categoria, Tecnologia, Proyecto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Proyecto)