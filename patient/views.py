from django.shortcuts import render, redirect
from .models import Paciente
from rest_framework import viewsets
from .serializer import PacienteSerializer
from django.contrib import messages
from django.views.generic import TemplateView
from . import views

# Create your views here.

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
# patient/views.py
from django.shortcuts import render, redirect
from .models import Paciente  # Certifique-se de importar sua classe de modelo

def cadastrar_paciente(request):
    if request.method == 'POST':
        # Processar os dados do formulário quando enviado
        cpf = request.POST['cpf']
        nome = request.POST['nome']
        datanasc = request.POST['datanasc']
        genero = request.POST['genero']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        email = request.POST['email']
        telefone = request.POST['telefone']

        # Criar um novo objeto Paciente e salvar no banco de dados
        paciente = Paciente(
            cpf=cpf,
            nome=nome,
            datanasc=datanasc,
            genero=genero,
            estado=estado,
            cidade=cidade,
            email=email,
            telefone=telefone
        )
        paciente.save()

        # Redirecionar para uma página de sucesso ou outra view
        return redirect('sucesso_cadastro')

    # Se o método não for POST, renderizar o formulário vazio
    return render(request, 'patient/cadastro_paciente.html')

class LoginPageView(TemplateView):
    template_name = 'patient/login.html'