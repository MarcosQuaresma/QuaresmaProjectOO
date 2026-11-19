from models.itens.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca): #<- pra herdar a classe "ItemBiblioteca" basta por dentro do ()
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)          #<- dessa maneira com o "super()" consigo recueprar diretamente 
        self.isbn = isbn # "isbn" uma subclasse especializada    # do construtor da classe pai, sem precisar ter que incluir novamente. 
                         # difere revista de livro.              # -> dentro da classe filha: class Livro():

        
        