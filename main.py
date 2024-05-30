import random
import time

inicio = time.time()
controle = 1

chaveP = (2**127)-1
chave = (2**127)-1
i = 1

while controle == 1:
  n = random.randrange(32,chaveP)
  t1 = pow(2,n-1,n)
  t2 = pow(3,n-1,n)
  t3 = pow(4,n-1,n)
  t4 = pow(5,n-1,n)
  t5 = pow(6,n-1,n)
  if (t1 == 1) and (t2 == 1) and (t3 == 1) and (t4 == 1) and (t5 == 1):
    P = n
    controle = 0
  else:
    controle = 1


print ("Valor de P :", P)

g = random.randrange(32,P-1)
print ("Valor de g : " , g)


a = random.randrange(127,chave)
b = random.randrange(127,chave)
print ("Valor de a : " , a)
print ("Valor de b : " , b)

A = pow(g,a,P)
B = pow(g,b,P)
print ("Chave A : " , A)
print ("Chave B : " , B)

k1 = pow(B,a,P)
k2 = pow(A,b,P)
print ("Chave simetrica k1 : " , k1)
print ("Chave simetrica k2 : " , k2)

while i == 1:
    a = random.randrange(127,chave)
    kebra1 = pow(B,a,P)

    if k1 == kebra1:
        print("Quebra a força concluida, senha: ", kebra1)
        break
    else:
        i == 1

fim = time.time()
tempo_total_segundos = fim - inicio
print ("O tempo total em segundos eh:" , tempo_total_segundos)
