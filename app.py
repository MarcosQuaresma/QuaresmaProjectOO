from models.biblioteca import Biblioteca #<- dessa maneira eu consigo utilizar somente a biblioteca desse arquivo.

biblioteca_Joinville = Biblioteca("Biblioteca de Joinville")
biblioteca_Shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_Joinville.alterna_estado()

def main():
    Biblioteca.listarBibliotecas() 

if __name__ == "__main__":
    main()