from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Usuario

def es_admin(user):
    return user.rol == 'admin'

@login_required
@user_passes_test(es_admin)
def panel_admin(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/panel_admin.html', {'usuarios': usuarios})

@login_required
def panel_aprendiz(request):
    return render(request, 'usuarios/panel_aprendiz.html', {'usuario': request.user})

def es_bienestar(user):
    return user.rol == 'bienestar'

@login_required
@user_passes_test(es_bienestar)
def panel_bienestar(request):
    aprendices = Usuario.objects.filter(rol='aprendiz')
    return render(request, 'usuarios/panel_bienestar.html', {'aprendices': aprendices})