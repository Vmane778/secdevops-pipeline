import os
import sys
from io import StringIO
from main import app  # Import the Flask app from main.py

# Simple WSGI adapter for Lambda
def lambda_handler(event, context):
    # Build WSGI environ from API Gateway event
    environ = {
        'REQUEST_METHOD': event.get('httpMethod', 'GET'),
        'SCRIPT_NAME': '',
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': event.get('queryStringParameters', {}) and '&'.join([f"{k}={v}" for k, v in event.get('queryStringParameters', {}).items()]) or '',
        'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
        'CONTENT_LENGTH': str(len(event.get('body', ''))),
        'SERVER_NAME': 'lambda',
        'SERVER_PORT': '80',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': StringIO(event.get('body', '')),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }

    # Add headers
    for header, value in event.get('headers', {}).items():
        environ[f'HTTP_{header.upper().replace("-", "_")}'] = value

    # Collect response
    status = []
    headers = []
    body = []

    def start_response(s, h, exc_info=None):
        status.append(s)
        headers.extend(h)

    # Call the WSGI app
    result = app.wsgi_app(environ, start_response)
    body.extend(result)

    # Return API Gateway response format
    return {
        'statusCode': int(status[0].split()[0]),
        'headers': dict(headers),
        'body': b''.join(body).decode('utf-8') if body and isinstance(body[0], bytes) else ''.join(body)
    }