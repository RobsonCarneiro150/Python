import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        user='root',
        password='090320',
        host='localhost',
        database='estoque_db'
    )

#CREATE-------------------------------------------------------------------------
def adicionar_produto(nome, quantidade, preco):
    conexao = conectar_bd()
    cursor = conexao.cursor()

    sql = "insert into produtos_tb (nome, quantidade, preco) values (%s, %s, %s)"
    valores = (nome, quantidade, preco)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f'Produto {nome} adicionado com suceso!')

    cursor.close()
    conexao.close()

#READ---------------------------------------------------------------------------
def listar_produtos():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute("select * from produtos_tb")
    resultados = cursor.fetchall()

    for i in resultados:
        print(f"ID: {i[0]}, Nome: {i[1]}, Quantidade: {i[2]}, Preço: {i[3]}")
    
    cursor.close()
    conexao.close()

#UPDATE-------------------------------------------------------------------------
def atualizar_produto(id, novo_nome, nova_quantidade, novo_preco):
    conexao = conectar_bd()
    cursor = conexao.cursor()

    sql = "UPDATE produtos_tb SET nome = %s, quantidade = %s, preco = %s WHERE id = %s"
    valores = (novo_nome, nova_quantidade, novo_preco, id)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f'Produto com ID {id} atualizado com sucesso!')

    cursor.close()
    conexao.close() 

#DELETE-------------------------------------------------------------------------
def deletar_produto(id):
    conexao = conectar_bd()
    cursor = conexao.cursor()

    sql = "DELETE FROM produtos_tb WHERE id = %s"
    valores = (id,)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f'Produto com ID {id} deletado com sucesso!')

    cursor.close()
    conexao.close()

def menu():
    while True:
        print("\n1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do Produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            adicionar_produto(nome, quantidade, preco)
        
        elif escolha == '2':
            listar_produtos()
        
        elif escolha == '3':
            id = int(input("ID do Produto: "))
            novo_nome = input("Novo Nome: ")
            nova_quantidade = int(input("Nova Quantidade: "))
            novo_preco = float(input("Novo Preço: "))
            atualizar_produto(id, novo_nome, nova_quantidade, novo_preco)
        
        elif escolha == '4':
            id = int(input("ID do Produto: "))
            deletar_produto(id)
        
        elif escolha == '5':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

