def main():
    t = Triangulo(1,2,3)
    print(t.perimetro())

class Triangulo:
    def __init__(self, a, b, c,):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c

main()


