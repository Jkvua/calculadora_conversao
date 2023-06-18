from tkinter import *
calculadora = Tk()
calculadora.title("Calculadora de conversão de Base - Camila BSI1")

pane = Frame(calculadora)
pane.pack(fill = BOTH, expand= True)

decimal_label = Label(calculadora, text="Decimal:")
num = int(input('Digite valor inteiro '))
#num vai pedir para a pessoa digitar um valor inteiro para que ele seja convertido para um número binario, octal ou hexadecimal
print("Escolha um base para conversão ")
print('1: BINÁRIO '
'2: OCTAL '
'3: HEXADECIMAL ')
#ao digitar o numero, tera que escolher para qual base decimal ira converter  
opcao = int(input("Sua opção "))
if opcao == 1:
    print('{} para número BINÁRIO é {} '.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} para número OCTAL é {} ' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} para número HEXADECIMAL é {} ' .format(num, hex(num)[2:]))
else:
    print('essa opção é invalida, tente novamente ')
#if,elif e else são usados para converter o numero caso nao seja a opção 1 seja a 2 caso não seja será a 3 se não for nenhuma a opção é invalida
#bin,oct,hex são funções que já vem com a python.
#os 2: são para pular duas casas depois da virgula.

calculadora.mainloop()