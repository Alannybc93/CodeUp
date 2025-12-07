# usuarios/views.py - VERSÃO SIMPLIFICADA
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Usuario

def registrar(request):
    """Página de cadastro"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        tipo = request.POST.get('tipo', 'ALUNO')
        
        # Validações básicas
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'usuarios/registrar.html')
        
        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'usuarios/registrar.html')
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso.')
            return render(request, 'usuarios/registrar.html')
        
        # Criar usuário
        try:
            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password1,
                tipo=tipo
            )
            
            # Login automático após cadastro
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {username}! Cadastro realizado com sucesso.')
                return redirect('home')
            else:
                messages.success(request, 'Conta criada com sucesso! Faça login.')
                return redirect('login')
                
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {str(e)}')
    
    return render(request, 'usuarios/registrar.html')

# REMOVA QUALQUER OUTRA FUNÇÃO COMO 'dashboard', 'home', etc.