from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario

def registrar(request):
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
        
        # Criar usuário
        try:
            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password1,
                tipo=tipo
            )
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {str(e)}')
    
    return render(request, 'usuarios/registrar.html')

@login_required
def dashboard(request):
    # Dashboard personalizado baseado no tipo de usuário
    user = request.user
    
    context = {
        'user': user,
        'pontos': user.pontos,
        'nivel': user.nivel,
        'tipo': user.get_tipo_display(),
    }
    
    # Redirecionar admin para painel admin
    if user.tipo == 'ADMIN':
        return redirect('admin_panel')
    
   
    return render(request, 'usuarios/dashboard.html', context)
# Configurações de Static Files
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'gamniceaco/static'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Templates
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'gamniceaco/templates')],
            'APP_DIRS': True,
            # ...
        },
    ]