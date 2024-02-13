from bottle import *

from pprint import pprint
import equations


@route("/")
def greeting():
    pprint(dict(request.headers))
    response.set_header('Vary', 'Accept')
    return '<h1>Welcome to my site !!!</h1>'


@route('/area/tri')
def area_tri():
    response.set_header('Vary', 'Accept')

    pprint(dict(request.query))

    try:

        length = int(request.query.get('length', '0'))
        width = int(request.query.get('width', '0'))

    except ValueError as e:

        return e.args[0]

    tri_area = equations.trian_area(length, width)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'

        return f'<p>The length is <em>{length}</em> and the width is <em> {width}</em>. The area of the triangle is <em>{tri_area}</em> </p>'

    return dict(length=length, width=width, area=tri_area, service=request.path)


@route('/area/rec')
def area_rec():
    response.set_header('Vary', 'Accept')

    pprint(dict(request.query))

    try:

        length = int(request.query.get('length', '0'))
        width = int(request.query.get('width', '0'))

    except ValueError as e:

        return e.args[0]

    rec_area = equations.rect_area(length, width)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'

        return f'<p>The length is <em>{length}</em> and the width is <em> {width}</em>. The area of the triangle is <em>{rec_area}</em> </p>'

    return dict(length=length, width=width, area=rec_area, service=request.path)


@route('/perm/tri')
def tri_perm():
    response.set_header('Vary', 'Accept')
    pprint(dict(request.query))

    try:

        length = int(request.query.get('length', '0'))
        width = int(request.query.get('width', '0'))
        height = int(request.query.get('height', '0'))

    except ValueError as e:

        return e.args[0]

    t_perimeter = equations.perm_tri(length, width, height)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'

        return f'<p>The side1 is <em>{length}</em> and the side2 is <em> {width}</em> and side 3 is {height}</em>. The area of the triangle is <em>{t_perimeter}</em> </p>'

    return dict(length=length, width=width, height=height,  perimeter=t_perimeter, service=request.path)


@route('/perm/rec')
def rec_perm():
    response.set_header('Vary', 'Accept')

    pprint(dict(request.query))

    try:

        length = int(request.query.get('length', '0'))
        width = int(request.query.get('width', '0'))

    except ValueError as e:

        return e.args[0]

    rec_perimeter = equations.perm_rec(length, width)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'

        return (f'<p>The length is <em>{length}</em> and the width is <em> {width}</em>. The perimeter of the '
                f'rectangle is <em>{rec_perimeter}</em> </p>')

    return dict(length=length, width=width, area=rec_perimeter, service=request.path)


if __name__ == "__main__":
    run(host='0.0.0.0', port="3000")
