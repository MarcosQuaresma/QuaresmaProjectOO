class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        self.ativo = False
        Biblioteca.bibliotecas.append(self)
    def __str__(self):
        return self.nome

    def listarBibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} - {biblioteca.ativo}")

bibliotecaJoinville = Biblioteca("Biblioteca de Joinville")
bibliotecaShopping =  Biblioteca("Biblioteca do Shopping")

print(bibliotecaShopping)
print(bibliotecaJoinville)

Biblioteca.listarBibliotecas()