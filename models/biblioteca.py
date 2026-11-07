class Biblioteca:
    bibliotecas = []
    def __init__(self, nome): #<-  Método contrutor: Assim que eu instanciar minha classe precio passar o nome dela (self,nome)
        self.nome = nome
        self._ativo = False # <- O modificador de visibilidade mais seguro é o "_" dentro do encapsulamento -> PRIVADO
        Biblioteca.bibliotecas.append(self)
    def __str__(self):        #<- Método que sobreescreve a informação quando o objeto for instanciado
        return self.nome

    @classmethod #"Decorador" muito ultilizado em orientação a objetos. nesse caso terei que usar o "(cls)" dentro da função definida.
    def listarBibliotecas(cls):  #<- Método que faz interação sobre os dados 
                                 #<- adicionando o "(cls)" referente a minha class
        print(f"{'Nome da biblioteca'.ljust(28)} - {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(28)} - {biblioteca.ativo}")

    def alterna_estado(self):  #<- esse seria o equivalente ao método set em Java
        self._ativo = not self._ativo # ele ta recebendo a negação "not" ou seja: se lá em cima na class Biblioteca estiver "True"
                                      # ele retorna "False" e vice e versa.
 
    @property #<- esse seria o método get em Java
    def ativo(self):
        return "Ativada" if self._ativo else "Desativada"

bibliotecaJoinville = Biblioteca("Biblioteca de Joinville")
bibliotecaShopping =  Biblioteca("Biblioteca do Shopping")

print(bibliotecaShopping)
print(bibliotecaJoinville)

bibliotecaJoinville.alterna_estado() #<- ele retorna o valor contrário que esta definido em uma função
bibliotecaShopping.alterna_estado()  #<- ele retorna o valor contrário que esta definido em uma função

Biblioteca.listarBibliotecas()