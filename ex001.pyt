#01 Fazer programa que converte a velocidade de m/s para km/h. Dado: velocidade(m/s) = velocidade(km/h) * 3.6
velocidade = float (input("Digite a velocidade em m/s: "))
vkm= velocidade*3.6
print ("A velocidade {} m/s é igual a {} Km/h ".format(velocidade, vkm))

#02 Fazer um programa em que o usuário digita o raio de um circunferência e o programa imprime na tela o seu comprimento.
import math 
raio = float (input("Digite o raio do círculo: "))
comprimento= float(2*math.pi*raio)
print ("O comprimento do circulo de raio %d é %.3f"%(raio, comprimento))

#03 Fazer um programa em qeue o usuário entra com um número e o programa imprime na tela seu antecessor e seu sucessor.
num = float (input("Digite um número:  "))
ant= num-1
suc= num+1
print ("O antecessor do número {} é {} e o sucessor é {}" .format(num, ant, suc))

#04 Fazer um programa em que o usuário entra com o ano de seu nascimento e o programa imprime na tela ssua idade.

anoN = int (input("Digite o ano em que você nasceu: "))
anoAtual = int (input("Digite o ano atual: "))
idade = anoAtual-anoN
print ("Sua idade é: ",idade, "anos")
