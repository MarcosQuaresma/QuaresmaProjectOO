from models.avaliacao import Avaliacao
from models.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []
    def __init__(self, nome): #<-  Método contrutor: Assim que eu instanciar minha classe precio passar o nome dela (self,nome)
        self.nome = nome
        self._ativo = False # <- O modificador de visibilidade mais seguro é o "_" dentro do encapsulamento -> PRIVADO
        self._avaliacao = []
        self._itens = [] #<- nessa lista eu posso adicionar quantos livros ou revista eu quiser.
    
        Biblioteca.bibliotecas.append(self)
    def __str__(self):        #<- Método que sobreescreve a informação quando o objeto for instanciado
        return self.nome

    @classmethod #"Decorador" muito ultilizado em orientação a objetos. nesse caso terei que usar o "(cls)" dentro da função definida.
    def listarBibliotecas(cls):  #<- Método que faz interação sobre os dados 
                                 #<- adicionando o "(cls)" referente a minha class
        print(f"{'Nome da biblioteca'.ljust(28)} | {'Nota Média'.ljust(28)} |{'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(28)} | {str(biblioteca.media_avaliacoes).ljust(28)} |{biblioteca.ativo}")
                                                    # nesse caso eu teria que converver ele para um "str()" pq o "ljust()" NÃO funciona
                                                    # em float
    def alterna_estado(self):  #<- esse seria o equivalente ao método set em Java
        self._ativo = not self._ativo # ele ta recebendo a negação "not" ou seja: se lá em cima na class Biblioteca estiver "True"
                                      # ele retorna "False" e vice e versa.
 
    @property #<- esse seria o método get em Java
    def ativo(self):
        return "Ativada" if self._ativo else "Desativada"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "█"
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media

    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)
    
    def exibit_itens(self):
        print(f"Itens da Biblioteca {self.nome}\n")
        for indice, item in enumerate(self._itens, start=1): #<- no "enumerate()" ele trás além do valor o indice da iteração.
            if hasattr(item, "isbn"):
                msg_livro = f"{indice}. (LIVRO)-> Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item.isbn}"
                print(msg_livro)
            else:
                msg_revista = f"{indice}. (REVISTA)-> Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edição: {item.edicao}"
                print(msg_revista)
