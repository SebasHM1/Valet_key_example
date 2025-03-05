from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.core.cache import cache
import uuid

# Página para solicitar clave
def request_key(request):
    if request.method == "POST":
        file_path = "protected/sample.pdf"  # Simulación de archivo
        key = str(uuid.uuid4())  # Genera una clave única
        expiration_time = 60  # Expira en 60 segundos

        # Guarda la clave en la caché
        cache.set(key, file_path, timeout=expiration_time)

        return render(request, "download.html", {"key": key})

    return render(request, "request_key.html")

# Descargar archivo con clave
def download_file(request, key):
    file_path = cache.get(key)

    if not file_path:
        return HttpResponseForbidden("La clave ha expirado o no es válida.")

    return HttpResponse(f"Descargando archivo: {file_path}")

# Verificar estado de la clave
def check_key_status(request, key):
    is_valid = cache.get(key) is not None
    return JsonResponse({"valid": is_valid})
