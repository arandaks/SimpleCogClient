from .use_cases import build_input_json, send_request

def client_factory(url):
    def client(inputs):
        input_json = build_input_json(inputs)
        response = send_request(url, input_json)
        return response        
    return client

