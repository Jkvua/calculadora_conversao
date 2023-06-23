import tkinter as tk

def converter():
    numero = int(entry_numero.get())
    opcao = int(var_opcao.get())
    base_entrada = (entry_num())
    base_saida = (entry_num())

    numero = input("Digite o número a ser convertido: ")
    base_entrada = int(input("Digite a base de entrada: "))
    base_saida = int(input("Digite a base de saída: "))


def converter_base(numero, base_entrada, base_saida):
    digitos_validos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Verifica se a base de entrada é válida
    if not 2 <= base_entrada <= 36:
        return "Erro: A base de entrada deve estar entre 2 e 36."

    # Verifica se a base de saída é válida
    if not 2 <= base_saida <= 36:
        return "Erro: A base de saída deve estar entre 2 e 36."

    # Verifica se o número está em conformidade com a base de entrada
    for digito in numero:
        if digito not in digitos_validos[:base_entrada]:
            return "Erro: O número não está em conformidade com a base de entrada escolhida."

    # Converte o número para base decimal
    decimal = int(numero, base_entrada)

    # Converte o número da base decimal para a base de saída
    resultado = ""
    while decimal > 0:
        resultado = digitos_validos[decimal % base_saida] + resultado
        decimal //= base_saida

    return resultado

calculadora = tk.Tk()
calculadora.title("Calculadora de conversão de base")
calculadora.geometry("400x300")

label_numero = tk.Label(calculadora, text="Digite um número a ser convertido")
label_numero.pack()

entry_numero = tk.Entry(calculadora)
entry_numero.pack()

resultado = converter_base(numero, base_entrada, base_saida)
print("Resultado: ", resultado)
