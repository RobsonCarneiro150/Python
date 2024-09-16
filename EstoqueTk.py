import mysql.connector
from tkinter import *
from tkinter import messagebox

# Conexão com o banco de dados
def conectar_bd():
    return mysql.connector.connect(
        user='root',
        password='090320',
        host='localhost',
        database='estoque_db'
    )

# Adicionar um produto
def adicionar_produto():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    nome = nome_entry.get()
    quantidade = int(quantidade_entry.get())
    preco = float(preco_entry.get())

    cursor.execute(
        "INSERT INTO produtos_tb (nome, quantidade, preco) VALUES (%s, %s, %s)",
        (nome, quantidade, preco)
    )
    conexao.commit()

    messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado com sucesso!")
    limpar_campos()
    listar_produtos()

    cursor.close()
    conexao.close()

# Listar produtos
def listar_produtos():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos_tb")
    produtos = cursor.fetchall()

    lista_produtos.delete(0, END)
    for produto in produtos:
        lista_produtos.insert(END, f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}")

    cursor.close()
    conexao.close()

# Atualizar um produto
def atualizar_produto():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    id = int(id_entry.get())
    novo_nome = nome_entry.get()
    nova_quantidade = int(quantidade_entry.get())
    novo_preco = float(preco_entry.get())

    cursor.execute(
        "UPDATE produtos_tb SET nome = %s, quantidade = %s, preco = %s WHERE id = %s",
        (novo_nome, nova_quantidade, novo_preco, id)
    )
    conexao.commit()

    messagebox.showinfo("Sucesso", f"Produto com ID {id} atualizado com sucesso!")
    limpar_campos()
    listar_produtos()

    cursor.close()
    conexao.close()

# Deletar um produto
def deletar_produto():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    id = int(id_entry.get())

    cursor.execute("DELETE FROM produtos_tb WHERE id = %s", (id,))
    conexao.commit()

    messagebox.showinfo("Sucesso", f"Produto com ID {id} deletado com sucesso!")
    limpar_campos()
    listar_produtos()

    cursor.close()
    conexao.close()

# Limpar campos de entrada
def limpar_campos():
    nome_entry.delete(0, END)
    quantidade_entry.delete(0, END)
    preco_entry.delete(0, END)
    id_entry.delete(0, END)

# Criação da interface gráfica
janela = Tk()
janela.title("Gestão de Estoque")

janela.grid_rowconfigure(0, weight=1)  # Linha 0 cresce proporcionalmente
janela.grid_columnconfigure(0, weight=1)  # Coluna 0 cresce proporcionalmente

# Rótulos
Label(janela, text="Nome do Produto").grid(row=0, column=0, padx=10, pady=5)
Label(janela, text="Quantidade").grid(row=1, column=0, padx=10, pady=5)
Label(janela, text="Preço").grid(row=2, column=0, padx=10, pady=5)
Label(janela, text="ID do Produto").grid(row=3, column=0, padx=10, pady=5)

nome_entry = Entry(janela)
quantidade_entry = Entry(janela)
preco_entry = Entry(janela)
id_entry = Entry(janela)

nome_entry.grid(row=0, column=1, pady=5)
quantidade_entry.grid(row=1, column=1, pady=5)
preco_entry.grid(row=2, column=1, pady=5)
id_entry.grid(row=3, column=1, pady=5)

lista_produtos = Listbox(janela, width=50)
lista_produtos.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

Button(janela, text="Adicionar Produto", command=adicionar_produto).grid(row=5, column=0, pady=5)
Button(janela, text="Atualizar Produto", command=atualizar_produto).grid(row=5, column=1)
Button(janela, text="Deletar Produto", command=deletar_produto).grid(row=6, column=0, pady=5)
Button(janela, text="Listar Produtos", command=listar_produtos).grid(row=6, column=1, pady=5)
Button(janela, text="Limpar Campos", command=limpar_campos).grid(row=7, column=0, columnspan=2, pady=5)

listar_produtos()  # Listar produtos ao iniciar a aplicação
janela.mainloop()
