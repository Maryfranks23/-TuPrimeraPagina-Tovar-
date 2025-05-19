from django.contrib import admin
from .models import Recarga, Cliente, EmpresaRecarga

admin.site.register(EmpresaRecarga)
admin.site.register(Cliente)
admin.site.register(Recarga) 