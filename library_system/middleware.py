import datetime

class BorrowLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == '/borrow/' and request.user.is_authenticated:
            print(f"{datetime.datetime.now()}: {request.user.username} visited borrow page")
        return response
