from models.biblioteca import Biblioteca #<- dessa maneira eu consigo utilizar somente a biblioteca desse arquivo.
from models.itens.livro import Livro
from models.itens.revista import Revista


biblioteca_Joinville = Biblioteca("Biblioteca de Joinville")
biblioteca_Shopping = Biblioteca("Biblioteca do Shopping")

livro01 = Livro("Windswept House: A Vatican Novel", "Malachi Martin", 367.00, "978-0385484084")
revista01 = Revista("The Economist", "James Wilson", 1704.00, "41")

# biblioteca_Joinville.alterna_estado()
# biblioteca_Joinville.receber_avaliacao("01 - Indivíduo", 8.5)
# biblioteca_Joinville.receber_avaliacao("02 - Indivíduo", 9.9)
# biblioteca_Joinville.receber_avaliacao("02 - Indivíduo", 7.9)

def main():
    # Biblioteca.listarBibliotecas() 
    print(vars(livro01))
    print(vars(revista01))

if __name__ == "__main__":
    main()