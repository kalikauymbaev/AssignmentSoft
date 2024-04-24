import Handler

class HardwareHandler(Handler):
    def handle_request(self, request):
        if request['type'] == 'hardware':
            return f"Hardware issue {request['id']} handled."
        else:
            return super().handle_request(request)

class SoftwareHandler(Handler):
    def handle_request(self, request):
        if request['type'] == 'software':
            return f"Software issue {request['id']} handled."
        else:
            return super().handle_request(request)

class NetworkHandler(Handler):
    def handle_request(self, request):
        if request['type'] == 'network':
            return f"Network issue {request['id']} handled."
        else:
            return super().handle_request(request)

# Setting up the chain
network_handler = NetworkHandler()
software_handler = SoftwareHandler(network_handler)
hardware_handler = HardwareHandler(software_handler)

# Test cases
test_requests = [
    {"id": 1, "type": "hardware", "description": "Laptop won't turn on"},
    {"id": 2, "type": "software", "description": "Cannot install software"},
    {"id": 3, "type": "network", "description": "Wifi connection issues"}
]

# Testing the chain of responsibility
for request in test_requests:
    print(hardware_handler.handle_request(request))