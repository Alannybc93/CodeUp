from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def lista_foruns(request):
    return render(request, "comunicacao/foruns.html")
