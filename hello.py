'''
Simple wsgi script
'''


def wsgi_application(environ, start_response):
    '''
    simple wsgi function
    '''
    
    status = "200 OK"

    headers = [
        ('Content-Type', 'text/plain'),
    ]

    body = 'Hello World'

    start_response(status, headers)

    return [body]

