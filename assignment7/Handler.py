class Handler:
    def __init__(self, next_handler=None):
        self._next_handler = next_handler
    
    def handle_request(self, request):
        if self._next_handler:
            return self._next_handler.handle_request(request)
        else:
            return f"Request {request['id']} could not be handled."