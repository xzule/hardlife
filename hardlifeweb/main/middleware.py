# from django.http import HttpResponseForbidden
# from django.urls import reverse
#
# class AdminIPRestrictionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         # Замените 'ALLOWED_IP' на ваш IP-адрес
#         allowed_ip = 'ALLOWED_IP'
#         client_ip = request.META.get('REMOTE_ADDR')
#
#         if request.path.startswith('/admin/') and client_ip != allowed_ip:
#             return HttpResponseForbidden("Доступ запрещен")
#
#         response = self.get_response(request)
#         return response