from datetime import datetime

class MiMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.hora_inicio = datetime.now()
        return self.get_response(request)