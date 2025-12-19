# usuarios/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Retorna um item de um dicionário"""
    return dictionary.get(key)

@register.filter
def multiply(value, arg):
    """Multiplica o valor pelo argumento"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def subtract(value, arg):
    """Subtrai o argumento do valor"""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def divide(value, arg):
    """Divide o valor pelo argumento"""
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def percentage(value, total):
    """Calcula porcentagem"""
    try:
        return (float(value) / float(total)) * 100
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def range_filter(value):
    """Cria um range para loops no template"""
    return range(value)

@register.filter
def add_str(value, arg):
    """Concatena strings"""
    return str(value) + str(arg)

@register.filter
def first_letters(value):
    """Retorna as primeiras letras do nome"""
    if not value:
        return ''
    parts = value.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[1][0]).upper()
    elif parts:
        return parts[0][0].upper()
    return ''

@register.filter
def file_exists(filefield):
    """Verifica se um campo de arquivo existe"""
    if filefield:
        try:
            return filefield.storage.exists(filefield.name)
        except:
            return False
    return False

@register.filter
def format_date(value, format_str='d/m/Y'):
    """Formata uma data"""
    if value:
        return value.strftime(format_str)
    return ''

@register.simple_tag
def active_page(request, view_name):
    """Verifica se a página atual corresponde ao view_name"""
    from django.urls import reverse, resolve
    
    try:
        # Obtém o nome da view atual
        current_view = resolve(request.path_info).view_name
        # Verifica se é a view desejada
        return 'active' if current_view == view_name else ''
    except:
        return ''