class Musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, seq, titulo):
        for i in range(len(seq)):
            if seq[i] == titulo:
                return i
        return -1
    
    def vamos_buscar(self):
        playlist = [
            Musica('Ponta de Areia', 'Milton Nascimento', 'Milton Nascimento', 1986),
            Musica('Podres Poderes', 'Caetano Veloso', 'Caetano Veloso', 1976),
            Musica('Baby', 'Gal Costa', 'Gal Costa', 1971)
        ]

        onde_achou = self.busca_por_titulo(playlist, 'Baby')

        if onde_achou == -1:
            print('A musica buscada não está na playlist')
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano, sep = '-')

b = Buscador()
b.vamos_buscar()


            