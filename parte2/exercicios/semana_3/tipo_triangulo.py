def main():
    t = Triangulo(5,8,5)
    print(t.tipo_lado())

class Triangulo:
    def __init__(self, a, b, c,):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if ((self.a == self.b) and (self.c != self.a) or (self.a == self.c) and (self.b != self.a)):
            return 'isósceles'
        elif (self.a == self.b == self.c):
            return 'equilátero'
        else:
            return 'escaleno'

main()


