import time
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import resolve, reverse

class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.request_time = {}
        self.responses_count = 0
        self.exception_count = 0
        # List of allowed URL names (not paths)
        self.allowed_url_names = ["login_app", "register"]

    def __call__(self, request: HttpRequest):
        time_delay = 5

        try:
            resolved_url = resolve(request.path_info)  # Resolve the URL
            url_name = resolved_url.url_name  # Extract URL name

            #Check if the resolved URL name is in the allowed list.
            if url_name not in self.allowed_url_names:
              return self.get_response(request) #Skip rate limiting if not in allowed URLs.

        except:
            # Handle cases where the URL cannot be resolved (e.g., 404)
            return self.get_response(request)

        if not self.request_time:
            print('first response')
        else:
            if (round(time.time())) - self.request_time['time'] < time_delay and \
               self.request_time['ip_address'] == request.META.get('REMOTE_ADDR'):
                print('Прошло меньше 1 секунды')
                return render(request, 'accounts/error-cournt-request.html')

        self.request_time = {'time': round(time.time()), 'ip_address': request.META.get('REMOTE_ADDR')}
        self.requests_count += 1

        response = self.get_response(request)
        self.responses_count += 1

        return response
