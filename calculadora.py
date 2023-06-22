import tkinter as tk

def converter():
   num = int(entry_num.get())
   opcao = int(var_opcao.get())

   if opcao == 1:
      resultado = bin(num)[2:]
   elif opcao == 2:
      resultado = oct(num)[2:]
   elif opcao == 3:
      resultado = hex(num)[2:]

   label_resultado.config(text="Resultado: " + resultado)

calculadora = tk.Tk()
calculadora.title("Calculadora de conversão de Base -  Camila BSI1")
calculadora.geometry("400x300")

label_num = tk.Label(calculadora, text="Digite um valor inteiro:")
label_num.pack()

entry_num = tk.Entry(calculadora)
entry_num.pack()

label_opcao = tk.Label(calculadora, text="Escolha uma das bases para conversão:")
label_opcao.pack()

var_opcao = tk.IntVar()

radio_binario = tk.Radiobutton(calculadora, text="Base Binária", variable=var_opcao, value=1)
radio_binario.pack()

radio_octal = tk.Radiobutton(calculadora, text="Base Octal", variable=var_opcao, value=2)
radio_octal.pack()

radio_hexadecimal = tk.Radiobutton(calculadora, text="Base Hexadecimal", variable=var_opcao, value=3)
radio_hexadecimal.pack()

btn_converter = tk.Button(calculadora, text="Converter", command=converter)
btn_converter.pack()

label_resultado = tk.Label(calculadora, text= f"O resultado para a base escolhida foi: ")
label_resultado.pack()

calculadora.mainloop()

