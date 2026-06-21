def parabola_approx(x1, x2, dt):
    i = x1
    area = 0
    while i < x2:
        area += dt*i**2
        i += dt

    return area

print(parabola_approx(0, 10, 0.000001))