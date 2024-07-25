import tkinter as tk
from tkinter import messagebox
from tarefas import adicionar_nova_tarefa, obter_tarefas, remover_uma_tarefa

def adicionar():
    tarefa = entrada_tarefa.get()
    print(f"Tarefa digitada: {tarefa}") 
    if tarefa:
        adicionar_nova_tarefa(tarefa)
        atualizar_lista()
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Digite uma tarefa.")

def remover():
    try:
        indice = lista_tarefas.curselection()[0]
        remover_uma_tarefa(indice)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Selecione uma tarefa para remover.")

def atualizar_lista():
    lista_tarefas.delete(0, tk.END)  
    for tarefa in obter_tarefas():
        lista_tarefas.insert(tk.END, tarefa)

# tkinter janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

# nova tarefa
frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=10)

entrada_tarefa = tk.Entry(frame_entrada, width=40)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

botao_adicionar = tk.Button(frame_entrada, text="Adicionar Tarefa", command=adicionar)
botao_adicionar.pack(side=tk.LEFT)

# Lista de tarefas
lista_tarefas = tk.Listbox(janela, width=50, height=10)
lista_tarefas.pack(pady=20)

# Botão de remover 
botao_remove = tk.Button(janela, text="Remover Tarefa", command=remover)
botao_remove.pack(pady=10)

# Inicia a interface
janela.mainloop()
