from tkinter import *

janela = Tk()
janela.title("Exemplo de Caixa de Texto")

# Função chamada ao pressionar o botão
def exibir_texto():
    texto = entrada.get()  # Obter o texto da caixa de texto
    label.config(text="Texto digitado: " + texto)

# Cria a caixa de texto
entrada = Entry(janela, width=30)
entrada.pack(pady=10)

# Cria o botão
botao = Button(janela, text="Exibir", command=exibir_texto)
botao.pack(pady=5)

# Cria um rótulo para exibir o resultado
label = Label(janela, text="")
label.pack(pady=10)

janela.mainloop()
