def soma (a,b):
    return a + b

def sub (a,b):
    return a - b

def mult (a,b):
    return a * b

def div (a,b):
    if b == 0:
        return "Não é possível dividir por 0"
    return a / b

def calc():

    print("-------Calculadora-------")
    num1 = float(input("Digite o primeiro número:  "))
    num2 = float(input("Digite o segundo número:  "))

    print("Escolha a operação a ser feita:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = (int(input("Digite a sua escolha:  ")))

    if escolha == 1:
        print( soma(num1,num2))
    elif escolha == 2:
        print( sub(num1,num2))
    elif escolha == 3 :
        print(mult(num1,num2))
    elif escolha == 4:
        print(div(num1,num2))
    else : 
        print("Digite um número válido")

calc()
