import tkinter as tk

def converter():
    num = int(entry_num.get())
    opcao = int(entry_opcao.get())
    
    if opcao == 1:
        resultado = format(num ,bin(num)[2:])
    elif opcao == 2:
        resultado = oct(num)[2:]
    elif opcao == 3:
        resultado = hex(num)[2:]
    else:
        resultado = 'Opção inválida'
    
    label_resultado.config(text="Resultado: " + resultado)

calculadora = tk.Tk()
calculadora.title("Calculadora de conversão de Base - Camila BSI1")
calculadora.geometry("400x400")

label_num = tk.Label(calculadora, text="Digite um valor inteiro:")
label_num.pack()

entry_num = tk.Entry(calculadora)
entry_num.pack()

label_opcao = tk.Label(calculadora, text="Escolha uma base para conversão:")
label_opcao.pack()

btn_button = tk.Button(text="Gerar QR Code", width=36, )
entry_opcao = tk.Entry(calculadora)
entry_opcao.pack()

btn_converter = tk.Button(calculadora, text="Converter", command=converter)
btn_converter.pack()

label_resultado = tk.Label(calculadora, text="Resultado:")
label_resultado.pack()

calculadora.mainloop()
