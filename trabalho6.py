#Integracao Numerica - Newton Cotes e Gauss-Legendre
#Universidade Federal do Ceara
#Metodos Numericos 2 - Prof. Creto Vidal
# Trabalho 6
#@franzejr - 0322836

from NewtonCotes import *
from GaussLegendre import *
import sys,math
from Funcao import *

def main():
	#Tratamento da Entrada
	if len(sys.argv) == 6:
		metodo = sys.argv[1]
		a = float(sys.argv[2])
		b = float(sys.argv[3])
		precisao1 = float(sys.argv[4])
		precisao2 = float(sys.argv[5])

	else:
		print "Trabalho 6 - Metodos Numericos - Exponencial Dupla e Simples\n"
		print "Voce deve inserir:<metodo> a b precisao1 precisao2\n"
		print  "<metodo> = trapezio, simpson, simpson38, boole, legendre\n"
		print "Se for NewtonCotes Aberto ou Fechado o programa ira perguntar depois\n"
		print "Se for Exponencial Simples ou Dupla o programa ira perguntar depois\n"
		return

	#Condicoes iniciais para o loop
	
	n=1
	valor_anterior=0
	#Setando a funcao para ser exponencial simples ou dupla
	funcao = Funcao(a,b,1)

	#Condicoes do loop
	condicao = 0.1
	condicao2 = 0.1
	valor_atual2 = 0
	valor_anterior2 = 0 
	alfa = 0.3

	if (metodo != "legendre"):
		
		aberto = raw_input("aberto[a]/fechado[f]? [a/f]:\n")
		
		#Saber se o Newton Cotes eh aberto ou fechado
		if (aberto == "a"):
			#Escolhendo qual metodo utilizar de acordo com o usuario
			if (metodo.lower() == "trapezio"):
				metodoIntegracao = TrapezioAberto()
			elif(metodo.lower() == "simpson"):
				metodoIntegracao = SimpsonAberto()
			elif(metodo.lower() == "simpson38"):
				metodoIntegracao = Simpson38Aberto()
			elif(metodo.lower() == "boole"):
				metodoIntegracao = BooleAberto()
		else:
			#Escolhendo os metodos de NewtonCotes Fechados
			if (metodo.lower() == "trapezio"):
				metodoIntegracao = Trapezio()
			elif(metodo.lower() == "simpson"):
				metodoIntegracao = Simpson()
			elif(metodo.lower() == "simpson38"):
				metodoIntegracao = Simpson38()
			elif(metodo.lower() == "boole"):
				metodoIntegracao = Boole()

		#Primeiro while para sabermos onde iremos cortar
		while(math.fabs(condicao) > precisao1):
			#Aumentando o fator alfa de 10 por cento
			alfa *= 1.1
			#Parametrizacao
			#Inicializando condicoes do while de dentro
			n = 1
			condicao2 = 1
			#While em relacao ao fator h
			while(math.fabs(condicao2) > precisao2 ):
				#resultadoIntegral*derivada
				valor_atual = metodoIntegracao.resolver(-alfa,alfa,n,funcao)
				condicao2 = valor_atual - valor_anterior
	   
				print  "particoes ",n,"alfa ",alfa ,"resultado: ",valor_atual
				valor_anterior = valor_atual
				n *= 2
			valor_atual2 = valor_atual
			condicao = valor_atual2 - valor_anterior2
			valor_anterior2 = valor_atual

	#Gauss Legendre
	else:
		#Instanciando um GaussLegendre
		metodoIntegracao = GaussLegendre(a,b)
		ai = metodoIntegracao.a
		bi = metodoIntegracao.b

		numPontos = int(raw_input("GaussLegendre com quantos pontos?? [2,3,4]:\n"))

		#Primeiro while para sabermos onde iremos cortar
		while(math.fabs(condicao) > precisao1):
			#Aumentando o fator alfa de 10 por cento
			alfa *= 1.1
			#Parametrizacao
			#Inicializando condicoes do while de dentro
			n = 1
			condicao2 = 1
			#While em relacao ao fator h
			while(math.fabs(condicao2) > precisao2 ):
				#resultadoIntegral*derivada
				tamanhoSubIntevalo = (alfa + alfa)/n
				valor_atual = metodoIntegracao.calcular(n,numPontos,tamanhoSubIntevalo,-alfa,alfa,funcao)
				condicao2 = valor_atual - valor_anterior
	   
				print  "particoes ",n,"alfa ",alfa ,"resultado: ",valor_atual
				valor_anterior = valor_atual
				n *= 2
			valor_atual2 = valor_atual
			condicao = valor_atual2 - valor_anterior2
			valor_anterior2 = valor_atual


main()