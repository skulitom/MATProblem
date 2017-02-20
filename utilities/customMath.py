

# http://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
def ccw(a, b, c):
    return (c.y-a.y) * (b.x-a.x) > (b.y-a.y) * (c.x-a.x)


# Return true if line segments AB and CD intersect
def intersect(a, b, c, d):
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)