""" Caluladora de Peso Ideal  
Fazer uma calculadora em que o usuário digita Altura em metros e Peso em quilos e se é do sexo biológico Masculino ou Feminino.
O programa devolve ao usuário a informação qual seu peso ideal e quando precisa emagrecer para chegar lá. Ao final, o programa deve trazer uma frase 
motivadora para aqueles que estão acima do peso, frase parabenizando os que estão no peso ideal e uma outra frase de alerta aos que estão abaixo do peso. 
Fórmulas
>Masculino: (72.7 * Altura) - 50
>Feminino: (62.1 * Altura) - 44.7"""

altura= float (input("Digite sua altura em metros: "))
peso= float (input("Digite seu peso em KG: "))
sexo = int( input("Digite 1 se for mulher e 2 se for homem:  ") )

if sexo == 1:
    pesoIdeal= (62.1 * altura) - 44.7
    print("Seu peso ideal seria {:.2f} Kg ".format (pesoIdeal))
    
if sexo==2:
    pesoIdeal= (72.7 * altura) - 50
    print("Seu peso ideal seria {:.2f} Kg".format (pesoIdeal))
    
diferenca= peso-pesoIdeal

if peso>pesoIdeal:
    print ("Você está acima do peso, se alimente melhor e perca uns %d quilinhos!" %(diferenca))

elif peso<pesoIdeal:
   print("Você está abaixo do peso, se alimente melhor e ganhe uns %d quilinhos!"%(diferenca)) 
    
else:
    print ("Parabéns, você está com o peso ideal!")
