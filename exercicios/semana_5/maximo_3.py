def maximo(x, y, z):
    if (x < y) and (z < y) :
        return y
    elif (y < x) and (z < x):
        return x
    else:
        return z