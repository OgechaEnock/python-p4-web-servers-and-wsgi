#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    # This prints the IP address of the client making the request
    print(f'This web server is running at {request.remote_addr}')
    # This sends back a simple HTTP response
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',  # server runs locally
        port=5555,             # port number (change if needed)
        application=application
    )
