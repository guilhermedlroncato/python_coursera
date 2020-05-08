def main():
    t1 = Triangulo(3, 4, 5)
    t2 = Triangulo(3, 4, 5)
    lt2 = sorted([t2.a, t2.b, t2.c])
    print(t1.semelhantes(lt2))

class Triangulo:
    def __init__(self, a, b, c,):
        self.a = a
        self.b = b
        self.c = c
        self.l = sorted([a, b, c])
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if ((self.a == self.b) and (self.c != self.a) or (self.a == self.c) and (self.b != self.a)):
            return 'isósceles'
        elif (self.a == self.b == self.c):
            return 'equilátero'
        else:
            return 'escaleno'
    
    def retangulo(self):
        hipotenusa =  0
        if self.a > self.b and self.a > self.c:
            hipotenusa = self.a
            cateto1 = self.b
            cateto2 = self.c
        elif self.b > self.a and self.b > self.c:
            hipotenusa = self.b
            cateto1 = self.a
            cateto2 = self.c
        else:
            hipotenusa = self.c
            cateto1 = self.a
            cateto2 = self.b
        
        if hipotenusa ** 2 == (cateto1 ** 2 + cateto2 ** 2):
            return True
        else:
            return False
    
    def semelhantes(self, t2):
        if (self.l[0]/t2[0]) == (self.l[1]/t2[1]) == (self.l[2]/t2[2]):
            return True
        else:
            return False

main()


