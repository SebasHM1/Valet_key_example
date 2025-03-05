from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
from django.utils.timezone import now
from .models import ValetKey
import uuid

# Página para solicitar clave
def request_key(request):
    if request.method == "POST":
        file_path = "protected/sample.pdf"  # Simulación de archivo
        valet_key = ValetKey.objects.create(file_path=file_path)
        return render(request, "download.html", {"key": valet_key.key})
    return render(request, "request_key.html")

# Descargar archivo con clave
def download_file(request, key):
    valet_key = get_object_or_404(ValetKey, key=key)
    
    if not valet_key.is_valid():
        return HttpResponseForbidden("La clave ha expirado.")

    return HttpResponse(f"Descargando archivo: {valet_key.file_path}")

from django.http import JsonResponse
from django.utils.timezone import now
from .models import ValetKey

def check_key_status(request, key):
    try:
        valet_key = ValetKey.objects.get(key=key)
        is_valid = valet_key.is_valid()
        return JsonResponse({"valid": is_valid})
    except ValetKey.DoesNotExist:
        return JsonResponse({"valid": False})

