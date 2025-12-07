from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ranking(request):
    return render(request, "gamificacao/ranking.html")
