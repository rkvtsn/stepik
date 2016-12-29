'''
Simple wsgi script
'''


def application(environ, start_response):
    '''
    simple wsgi function
    '''

    status = "200 OK"

    headers = [
        ('Content-Type', 'text/plain'),
    ]

    body = "Helloo" #environ['QUERY_STRING']

    start_response(status, headers)

    return [body]

