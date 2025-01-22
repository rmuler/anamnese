import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Função para salvar os dados na planilha Excel
def salvar_dados():
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    historico_doencas = entry_historico.get()

    if not nome or not data_nascimento or not historico_doencas:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
        return

    # Organizar os dados em um dicionário
    dados = {
        'Nome': [nome],
        'Data de Nascimento': [data_nascimento],
        'Histórico de Doenças': [historico_doencas]
    }

    # Converter o dicionário para um DataFrame do pandas
    df = pd.DataFrame(dados)

    # Se o arquivo já existir, adiciona os dados sem sobrescrever
    if os.path.exists("cadastro_anamnese.xlsx"):
        df_existente = pd.read_excel("cadastro_anamnese.xlsx")
        df = pd.concat([df_existente, df], ignore_index=True)

    # Salvar os dados no arquivo Excel
    df.to_excel("cadastro_anamnese.xlsx", index=False)

    # Exibir mensagem de sucesso
    messagebox.showinfo("Sucesso", "Dados armazenados com sucesso!")

    # Limpar os campos de entrada após salvar
    entry_nome.delete(0, tk.END)
    entry_data_nascimento.delete(0, tk.END)
    entry_historico.delete(0, tk.END)

# Função para criar a janela do Tkinter
def criar_janela():
    janela = tk.Tk()
    janela.title("Cadastro de Anamnese")
    
    # Definir tamanho da janela
    janela.geometry("400x300")
    
    # Rótulos e campos de entrada
    tk.Label(janela, text="Nome completo:").pack(pady=5)
    global entry_nome
    entry_nome = tk.Entry(janela, width=50)
    entry_nome.pack(pady=5)

    tk.Label(janela, text="Data de nascimento (DD/MM/AAAA):").pack(pady=5)
    global entry_data_nascimento
    entry_data_nascimento = tk.Entry(janela, width=50)
    entry_data_nascimento.pack(pady=5)

    tk.Label(janela, text="Histórico de Doenças:").pack(pady=5)
    global entry_historico
    entry_historico = tk.Entry(janela, width=50)
    entry_historico.pack(pady=5)

    # Botão para salvar os dados
    tk.Button(janela, text="Salvar Dados", command=salvar_dados).pack(pady=20)

    # Iniciar o loop principal
    janela.mainloop()

# Executar o programa
if __name__ == "__main__":
    criar_janela()