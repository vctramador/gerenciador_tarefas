print("tarefas.py carregado")

lista_de_tarefas = []

def adicionar_nova_tarefa(tarefa):
    if tarefa:
        lista_de_tarefas.append(tarefa)

def obter_tarefas():
    return lista_de_tarefas

def remover_uma_tarefa(indice):
    if 0 <= indice < len(lista_de_tarefas):
        lista_de_tarefas.pop(indice)
