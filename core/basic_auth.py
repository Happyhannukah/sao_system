from django.http import HttpResponse
import base64

def basic_auth_middleware(get_response):
    def middleware(request):
        # Change these to the username/password you want
        username = "092621"
        password = "labblabb"

        # Check for Authorization header
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Basic '):
            encoded_credentials = auth_header.split(' ')[1]
            decoded_bytes = base64.b64decode(encoded_credentials).decode('utf-8')
            req_username, req_password = decoded_bytes.split(':', 1)

            if req_username == username and req_password == password:
                return get_response(request)

        # If no valid auth, send back 401 response
        response = HttpResponse('Unauthorized', status=401)
        response['WWW-Authenticate'] = 'Basic realm="SAO System"'
        return response

    return middleware
