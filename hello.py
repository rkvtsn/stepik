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

    start_response(status, headers)

    if environ.contains('QUERY_STRING'):
        return environ['QUERY_STRING'].split("&")
    else:
        return [""]

