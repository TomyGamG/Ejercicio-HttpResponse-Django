from django.shortcuts import render
from django.http import HttpResponse, QueryDict, JsonResponse, StreamingHttpResponse, FileResponse
from django.http.response import HttpResponseBase
from django.conf import settings
import time, os

def index(request):
    return render(request, 'request/request.html')
def request_page(request):
    metodo = request.method
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT', 'Desconocido')
    path = request.path

    return HttpResponse(f"""
        <h1>Información de la Solicitud</h1>
        <p><strong>Método:</strong> {metodo}</p>
        <p><strong>IP del cliente:</strong> {ip}</p>
        <p><strong>User-Agent:</strong> {user_agent}</p>
        <p><strong>Ruta solicitada:</strong> {path}</p>
    """)
def app_atributes(request):
    app_name = "HTTPResponse"
    return render(request, 'request/app-atributes.html', {'app_name': app_name})
def middleware(request):
    valor = getattr(request, 'hora_inicio', 'Atributo no encontrado')
    return HttpResponse(f"<h1>{valor}</h1>")
def querydict(request):
    parametros_get = request.GET
    datos_post = QueryDict('nombre=Juan&nombre=Lucía&edad=30')
    contenido = "<h2>QueryDicts</h2>"
    contenido += "<h3>Parámetros por GET:</h3>"
    for clave in parametros_get:
        contenido += f"<p>{clave}: {parametros_get.getlist(clave)}</p>"

    contenido += "<h3>QueryDict simulado:</h3>"
    for clave in datos_post:
        contenido += f"<p>{clave}: {datos_post.getlist(clave)}</p>"

    return HttpResponse(contenido)
def is_secure(request):
    if request.is_secure():
        return HttpResponse("La conexión es segura (HTTPS).")
    else:
        return HttpResponse("La conexión NO es segura (HTTP).")
def home(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        mensaje = f"Hola, {nombre}. Has enviado un formulario con POST."
        return render(request, 'request/home.html', {'mensaje': mensaje})
    else:
        return render(request, 'request/home.html')
def response(request):
    return HttpResponse("Esto es una respuesta basica usando HttpResponse")
def subclasses(request):
    response = HttpResponse("Esta respuesta tiene un encabezado personalizado.")
    response['X-Ejemplo-Encabezado'] = 'Hola Mundo'
    return response
def json(request):
    datos = {
        'mensaje': 'Hola desde una respuesta JSON',
        'estado': 'ok',
        'codigo': 200
    }
    return JsonResponse(datos)
def streaming(request):
    return StreamingHttpResponse(generador(), content_type="text/html")
def file(request):
    ruta_imagen = os.path.join(settings.BASE_DIR, 'request', 'imagen', 'tanji.jpg')
    return FileResponse(open(ruta_imagen, 'rb'), content_type='image/jpg')
def base(request):
    return HttpResponse("Usando HttpResponseBase correctamente(En realidad es HttpResponse porque el Base me da conflicto con .streaming)", content_type="text/plain")
def generador():
    for i in range(5):
        yield f"Parte {i + 1}\n"