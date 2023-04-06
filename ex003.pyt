"""Meta de vendas: 50.000 unidades.
Usuário vai informar quantas unidades do produto foram vendidas.
Se a meta não for atingida, o programa deverá informar que a meta não foi atingida e ninguém recebe bonus.
Se a meta for atingida com menos de 500 unidades de diferença, o programa informa que a meta foi atingida e que os vendedores ganharão 5% de bonus.
Se a meta for ultrapassada em mais de 500 unidades, os vendedores receberão bonus de 15%"""

meta=50000
vendas = int (input("Informe quantas unidades do produto você vendeu?"))
if vendas==meta-500:
     print ("Sua meta foi atingida, você ganhou um bônus de 5%")
elif vendas== meta + 500:
     print ("Sua meta foi atingida, você ganhou um bônus de 15% ")
else:
     print ("Sua meta não foi atingida")
