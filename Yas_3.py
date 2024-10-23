from tkinter import messagebox 
import tkinter as tk

# Criação da janela principal
janela = tk.Tk()
janela.title("Exemplo de Imagem com PhotoImage")

# Carrega a imagem (apenas PNG ou GIF)
imagem = tk.PhotoImage(file="ahrianime.GIF")

# Criação de um rótulo (Label) com a imagem
rotulo = tk.Label(janela, image=imagem)
rotulo.pack()
rotulo01 = tk.Label(janela, text="Interface gráfica com imagem")
rotulo01.pack ()

def mostrar_mensagem():
 messagebox.showinfo("informação", "Botão Clicado")

botaolol = tk.PhotoImage(file="botaoclique.png")
botao = tk.Button(janela, image= botaolol, command=mostrar_mensagem)
botao.pack()

# Mantém a janela aberta
janela.mainloop()



