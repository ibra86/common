from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now as django_now


class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_render_time = django_now()

    def process_response(self, request, response):
        finish_time = django_now()
        result = finish_time - request.start_render_time
        print(f'request {request} was processed {result.microseconds} m-seconds')
        return response
