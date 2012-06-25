#Funcao Generica para calculo do Xi
#intervaloA: inicio do intervalo A
#intervaloB: final da parte onde vamos integrar
#i: qual Xi queremos. Ex.: x0, x1...xN
#numIntervalos: Se o polinomio eh de grau n fechado, entao teremos 2 intervalos, por exemplo, n-1 intervalos, n+1 pontos
############### Se o polinomio eh de grau n aberto, n+2 intervalos, n+1 pontos
def calcularXi(intervaloA, intervaloB, i, numIntervalos):
        return intervaloA + i * (intervaloB - intervaloA) / numIntervalos