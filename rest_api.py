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

    tri_area = equations.area_tri(length, width)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'

        return f'<p>The length is <em>{length}</em> and the width is <em> {width}</em>. The area of the triangle is <em>{tri_area}</em> </p>'

    return dict(length=length, width=width, area=tri_area, service=request.path)


@route('/perm/tri')
def tri_perm():
    response.set_header('Vary', 'Accept')
    pprint(dict(request.query))

    try:

        side1 = int(request.query.get('side 1', '0'))
        side2 = int(request.query.get('side 2', '0'))
        side3 = int(request.query.get("side 3", '0'))

    except ValueError as e:

        return e.args[0]

    tri_perimeter = equations.perm_tri(side1, side2, side3)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'

        return (f'<p>Side 1 is <em>{side1}</em> and the side 2 is <em> {side2}</em> and the last side is<em{side3}</em'
                f'>. The perimeter of the triangle is <em>{tri_perimeter}</em> </p>')

    return dict(side1=side1, side2=side2, side3=side3, perimeter=tri_perimeter, service=request.path)


@route('/perm/rec')
def rec_perm():
    response.set_header('Vary', 'Accept')

    pprint(dict(request.query))

    try:

        length = int(request.query.get('length', '0'))
        width = int(request.query.get('width', '0'))

    except ValueError as e:

        return e.args[0]

    rec_perimeter = equations.perim_rec(length, width)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'

        return (f'<p>The length is <em>{length}</em> and the width is <em> {width}</em>. The perimeter of the '
                f'rectangle is <em>{rec_perimeter}</em> </p>')

    return dict(length=length, width=width, area=rec_perimeter, service=request.path)


if __name__ == "__main__":
    run(host='0.0.0.0', port="3000")
