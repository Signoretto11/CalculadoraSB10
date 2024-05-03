def add(x,y):
  return x + y

def sub(x,y):
  return x - y

def mult(x,y):
  return x * y

def div(x,y):
  return x / y

print("Selecione uma operação.")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha uma operação (1/2/3/4)")
N1 = float(input("digite um número: "))
N2 = float(input("digite outro número: "))

if escolha in ('1','2','3','4'):
  if escolha == '1':
    print(N1, "+",N2, "=", add(N1,N2))
    print(add(N1,N2))

  if escolha == '2':
    print(sub(N1,N2))

  if escolha == '3':
    print(mult(N1,N2))

  if escolha == '4':
    print(div(N1,N2))
    
  

               