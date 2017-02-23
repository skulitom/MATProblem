def ccw(a, b, c):
    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])


# Return true if line segments AB and CD intersect
def intersect(a, b, c, d):

    if a == c or a == d or b == c or b == d:
        return True

    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


def modified_intersect(a, b, c, d):

    if a == c or a == d or b == c or b == d:
        return False

    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)
