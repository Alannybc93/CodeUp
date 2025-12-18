from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import Usuario

Usuario = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome de usuário',
            'class': 'form-input'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Senha',
            'class': 'form-input'
        })
    )

class RegistrarForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'first_name', 'last_name', 'email', 'foto',
            'bio', 'cidade', 'estado', 'website'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'foto':
                field.widget.attrs.update({'class': 'form-input'})

class AlterarSenhaForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

class ConfigurarContaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'tema_escuro', 'receber_notificacoes', 'receber_newsletter',
            'email_publico'
        ]
        widgets = {
            'tema_escuro': forms.CheckboxInput(),
            'receber_notificacoes': forms.CheckboxInput(),
            'receber_newsletter': forms.CheckboxInput(),
            'email_publico': forms.CheckboxInput(),
        }