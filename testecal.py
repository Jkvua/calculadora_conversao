import tkinter as tk

def converter_base(numero, base_entrada, base_saida):
    digitos_validos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not 2 <= base_entrada <= 16:
        return "A base de entrada deve estar entre 2 e 16."

    if not 2 <= base_saida <= 16:
        return "A base de saída deve estar entre 2 e 16."

    for digito in numero:
        if digito not in digitos_validos[:base_entrada]:
            return "O número não está em conformidade com a base de entrada escolhida."

    decimal = int(numero, base_entrada)

    resultado = ""
    while decimal > 0:
        resultado = digitos_validos[decimal % base_saida] + resultado
        decimal //= base_saida

    return resultado

def converter():
    numero = entry_numero.get()
    baseentrada = int(entry_baseentrada.get())
    base_saida = int(entry_base_saida.get())

    resultado = converter_base(numero, baseentrada, base_saida)
    label_resultado["text"] = "Resultado: " + resultado

calculadora = tk.Tk()
calculadora.title("Calculadora de conversão de base")
calculadora.geometry("600x300")

label_numero = tk.Label(calculadora, text="Digite um número a ser convertido:")
label_numero.pack()

entry_numero = tk.Entry(calculadora)
entry_numero.pack()

label_baseentrada = tk.Label(calculadora, text="Digite a base de entrada para conversão:")
label_baseentrada.pack()

entry_baseentrada = tk.Entry(calculadora)
entry_baseentrada.pack()

label_base_saida = tk.Label(calculadora, text="Digite a base de saída para conversão:")
label_base_saida.pack()

entry_base_saida = tk.Entry(calculadora)
entry_base_saida.pack()

botao_converter = tk.Button(calculadora, text="Converter", command=converter)
botao_converter.pack()

label_resultado = tk.Label(calculadora, text="Resultado: ")
label_resultado.pack()

calculadora.mainloop()
