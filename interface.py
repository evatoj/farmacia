import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from CRUD import *


def personalizado(style):
    style.configure('Custom.TButton',
                    background='#007bff',
                    foreground='white',
                    borderwidth=1,
                    relief='solid',
                    width=20)
    style.map('Custom.TButton',
              background=[('active', '#0056b3')],
              foreground=[('active', 'white')])
    style.configure('Treeview', font=("Helvetica", 10))
    style.configure('Treeview.Heading', font=("Helvetica", 12, "bold"))


def janela_inserir_medicamento():
    inserir_window = ttk.Toplevel()
    inserir_window.title("Inserir Medicamento")
    inserir_window.geometry("500x400")

    ttk.Label(inserir_window, text="Nome do Medicamento:",
              font=("Helvetica", 10, "bold")).pack(pady=10)
    nome_entry = ttk.Entry(inserir_window, font=("Helvetica", 10))
    nome_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(inserir_window, text="Fabricante:", font=(
        "Helvetica", 10, "bold")).pack(pady=10)
    fabricante_entry = ttk.Entry(inserir_window, font=("Helvetica", 10))
    fabricante_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(inserir_window, text="Quantidade:", font=(
        "Helvetica", 10, "bold")).pack(pady=10)
    quantidade_entry = ttk.Entry(inserir_window, font=("Helvetica", 10))
    quantidade_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(inserir_window, text="Valor:", font=(
        "Helvetica", 10, "bold")).pack(pady=10)
    valor_entry = ttk.Entry(inserir_window, font=("Helvetica", 10))
    valor_entry.pack(pady=5, padx=20, fill=X)

    def inserir():
        nome = nome_entry.get()
        fabricante = fabricante_entry.get()
        quantidade = int(quantidade_entry.get())
        valor = float(valor_entry.get())
        mensagem = criar_medicamento(nome, fabricante, quantidade, valor)
        messagebox.showinfo("Resultado", mensagem)
        inserir_window.destroy()

    ttk.Button(inserir_window, text="Inserir",
               style="Custom.TButton", command=inserir).pack(pady=20, fill=X, padx=20)


def janela_alterar_medicamento():
    alterar_window = ttk.Toplevel()
    alterar_window.title("Alterar Medicamento")
    alterar_window.geometry("500x400")

    alterar_window.configure(background='#2e2e2e')

    ttk.Label(alterar_window, text="ID do Medicamento:",
              font=("Helvetica", 10, "bold"), background='#2e2e2e', foreground='white').pack(pady=10)
    id_entry = ttk.Entry(alterar_window, font=("Helvetica", 10))
    id_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(alterar_window, text="Coluna para alterar:", font=(
        "Helvetica", 10, "bold"), background='#2e2e2e', foreground='white').pack(pady=10)

    coluna_selecionada = tk.StringVar(value='nome_medicamento')
    coluna_menu = ttk.Combobox(alterar_window, textvariable=coluna_selecionada,
                               values=["nome_medicamento", "fabricante", "quantidade", "valor"], font=("Helvetica", 10))
    coluna_menu.pack(pady=5, padx=20, fill=X)

    ttk.Label(alterar_window, text="Novo Valor:", font=(
        "Helvetica", 10, "bold"), background='#2e2e2e', foreground='white').pack(pady=10)
    valor_entry = ttk.Entry(alterar_window, font=("Helvetica", 10))
    valor_entry.pack(pady=5, padx=20, fill=X)

    def alterar():
        id_medicamento = int(id_entry.get())
        coluna = coluna_selecionada.get()
        novo_valor = valor_entry.get()

        if coluna == "quantidade":
            novo_valor = int(novo_valor)
        elif coluna == "valor":
            novo_valor = float(novo_valor)

        mensagem = alterar_medicamento(id_medicamento, coluna, novo_valor)
        messagebox.showinfo("Resultado", mensagem)
        alterar_window.destroy()

    ttk.Button(alterar_window, text="Alterar", style="Custom.TButton",
               command=alterar).pack(pady=20, fill=X, padx=20)


def janela_buscar_por_nome():
    buscar_window = ttk.Toplevel()
    buscar_window.title("Buscar Medicamento por Nome")
    buscar_window.geometry("700x400")

    ttk.Label(buscar_window, text="Nome do Medicamento:",
              font=("Helvetica", 10, "bold")).pack(pady=10)
    nome_entry = ttk.Entry(buscar_window, font=("Helvetica", 10))
    nome_entry.pack(pady=5, padx=20, fill=X)

    resultado_tree = ttk.Treeview(buscar_window, columns=(
        "ID", "Nome", "Fabricante", "Quantidade", "Valor"), show='headings')
    resultado_tree.heading("ID", text="ID")
    resultado_tree.heading("Nome", text="Nome")
    resultado_tree.heading("Fabricante", text="Fabricante")
    resultado_tree.heading("Quantidade", text="Quantidade")
    resultado_tree.heading("Valor", text="Valor")

    resultado_tree.tag_configure(
        'default', background='#2e2e2e', foreground='white')
    resultado_tree.pack(pady=20, padx=20, fill=BOTH, expand=True)

    def buscar():
        nome = nome_entry.get()
        resultados = buscar_por_nome(nome)
        resultado_tree.delete(*resultado_tree.get_children())
        if resultados:
            for medicamento in resultados:
                resultado_tree.insert(
                    '', 'end', values=medicamento, tags=('default',))
        else:
            messagebox.showinfo(
                "Resultado", "Nenhum medicamento encontrado com o nome especificado.")

    ttk.Button(buscar_window, text="Buscar", style="Custom.TButton",
               command=buscar).pack(pady=20, fill=X, padx=20)


def janela_remover_medicamento():
    remover_window = ttk.Toplevel()
    remover_window.title("Remover Medicamento")
    remover_window.geometry("400x250")

    ttk.Label(remover_window, text="ID do Medicamento:",
              font=("Helvetica", 10, "bold")).pack(pady=10)
    id_entry = ttk.Entry(remover_window, font=("Helvetica", 10))
    id_entry.pack(pady=5, padx=20, fill=X)

    def remover():
        id_medicamento = int(id_entry.get())
        mensagem = remover_medicamento(id_medicamento)
        messagebox.showinfo("Resultado", mensagem)
        remover_window.destroy()

    ttk.Button(remover_window, text="Remover", style="Custom.TButton",
               command=remover).pack(pady=20, fill=X, padx=20)


def janela_exibir_todos():
    exibir_window = ttk.Toplevel()
    exibir_window.title("Todos os Medicamentos")
    exibir_window.geometry("700x400")

    tree = ttk.Treeview(exibir_window, columns=(
        "ID", "Nome", "Fabricante", "Quantidade", "Valor"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Fabricante", text="Fabricante")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Valor", text="Valor")

    tree.tag_configure('default', background='#2e2e2e', foreground='white')

    resultado = exibir_todos()
    for medicamento in resultado:
        tree.insert('', 'end', values=medicamento, tags=('default',))

    tree.pack(pady=20, padx=20, fill=BOTH, expand=True)

    ttk.Button(exibir_window, text="Voltar", style="Custom.TButton",
               command=exibir_window.destroy).pack(pady=20, fill=X, padx=20)


def janela_exibir_um():
    exibir_window = ttk.Toplevel()
    exibir_window.title("Exibir Medicamento por ID")
    exibir_window.geometry("400x300")

    ttk.Label(exibir_window, text="ID do Medicamento:",
              font=("Helvetica", 10, "bold")).pack(pady=10)
    id_entry = ttk.Entry(exibir_window, font=("Helvetica", 10))
    id_entry.pack(pady=5, padx=20, fill=X)

    resultado_label = ttk.Label(exibir_window, text="", font=("Helvetica", 10))
    resultado_label.pack(pady=20)

    def exibir():
        id_medicamento = int(id_entry.get())
        resultado = exibir_um(id_medicamento)
        if resultado:
            medicamento = resultado[0]
            id_medicamento, nome, fabricante, quantidade, valor = medicamento

            texto_resultado = (
                f"ID: {id_medicamento}\n"
                f"Nome: {nome}\n"
                f"Fabricante: {fabricante}\n"
                f"Quantidade: {quantidade}\n"
                f"Valor: {valor}"
            )
            resultado_label.config(text=texto_resultado)
        else:
            resultado_label.config(text="Medicamento não encontrado.")

    ttk.Button(exibir_window, text="Exibir", style="Custom.TButton",
               command=exibir).pack(pady=20, fill=X, padx=20)


def interface_principal():
    app = ttk.Window(themename="darkly")
    app.title("Sistema de Farmácia")
    app.geometry("600x600")

    style = ttk.Style()
    personalizado(style)

    titulo = ttk.Label(app, text="Escolha uma opção", font=(
        "Lucida Console", 36, "bold"), foreground="white")
    titulo.pack(pady=20)

    ttk.Button(app, text="Inserir Medicamento", style="Custom.TButton",
               command=janela_inserir_medicamento).pack(fill=X, padx=20, pady=10)
    ttk.Button(app, text="Alterar Medicamento", style="Custom.TButton",
               command=janela_alterar_medicamento).pack(fill=X, padx=20, pady=10)
    ttk.Button(app, text="Buscar por Nome", style="Custom.TButton",
               command=janela_buscar_por_nome).pack(fill=X, padx=20, pady=10)
    ttk.Button(app, text="Remover Medicamento", style="Custom.TButton",
               command=janela_remover_medicamento).pack(fill=X, padx=20, pady=10)
    ttk.Button(app, text="Exibir Todos", style="Custom.TButton",
               command=janela_exibir_todos).pack(fill=X, padx=20, pady=10)
    ttk.Button(app, text="Exibir Um Medicamento", style="Custom.TButton",
               command=janela_exibir_um).pack(fill=X, padx=20, pady=10)
    ttk.Button(app, text="Sair", style="Custom.TButton",
               command=app.quit).pack(fill=X, padx=20, pady=10)

    app.mainloop()


if __name__ == "__main__":
    interface_principal()
