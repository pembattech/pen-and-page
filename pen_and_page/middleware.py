from django.shortcuts import redirect
from django.urls import reverse


class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/admin/' and request.user.is_authenticated and not request.user.is_superuser:
            # Replace 'home' with the name of your home page URL
            return redirect(reverse('home'))
        return self.get_response(request)
