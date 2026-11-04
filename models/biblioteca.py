class Biblioteca:
    nome = ""
    ativo = False

bibliotecaCidade = Biblioteca()
bibliotecaCidade.nome = "Biblioteca da Cidade"
bibliotecaCidade.ativo = True

bibliotecaShopping = Biblioteca()

listaBibliotecas = [bibliotecaShopping, bibliotecaCidade] #<- dessa maneira teremos que utilizar o loop "for x in y:"

print(vars(bibliotecaCidade)) # <- quando eu cham o "vars()" ele me retorna em fromato de dicinário {}
                              # e as informações que tem dentro do objeto 
print(vars(bibliotecaShopping))

for x in listaBibliotecas:
    print(vars(x))