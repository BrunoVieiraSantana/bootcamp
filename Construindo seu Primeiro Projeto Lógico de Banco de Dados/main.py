import sqlite3

def conectar_banco_dados():
    return sqlite3.connect('ecommerce.db')

def setup_banco_dados():

    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamentos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            forma_pagamento TEXT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entregas (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            codigo_rastreio TEXT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        )
    ''')

    conn.commit()
    conn.close()

def adicionar_cliente(nome, tipo):
    conn = conectar_banco_dados()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clientes (nome, tipo) VALUES (?, ?)', (nome, tipo))
    conn.commit()
    conn.close()

def recuperar_clientes():
    conn = conectar_banco_dados()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def filtrar_clientes(tipo_cliente):
    conn = conectar_banco_dados()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE tipo = ?', (tipo_cliente,))
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def criar_atributo_derivado():
    conn = conectar_banco_dados()
    cursor = conn.cursor()

    cursor.execute('SELECT *, (SELECT COUNT(*) FROM pagamentos WHERE pagamentos.cliente_id = clientes.id) AS total_pagamentos FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def ordenar_clientes_por_nome():
    conn = conectar_banco_dados()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes ORDER BY nome')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def filtrar_clientes_por_pagamento(forma_pagamento):
    conn = conectar_banco_dados()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT clientes.* FROM clientes
        INNER JOIN pagamentos ON clientes.id = pagamentos.cliente_id
        WHERE pagamentos.forma_pagamento = ?
    ''', (forma_pagamento,))
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def main():
    setup_banco_dados()
    
    while True:
        print("\n===== MENU INTERATIVO =====")
        print("1 - Recuperar todos os clientes")
        print("2 - Filtrar clientes por tipo (PJ ou PF)")
        print("3 - Criar atributo derivado (exemplo: total de pagamentos)")
        print("4 - Ordenar clientes por nome")
        print("5 - Filtrar clientes por forma de pagamento")
        print("6 - Adicionar novo cliente")
        print("0 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            clientes = recuperar_clientes()
            print("\n===== CLIENTES =====")
            for cliente in clientes:
                print(cliente)

        elif opcao == "2":
            tipo_cliente = input("Digite o tipo de cliente (PJ ou PF): ")
            clientes = filtrar_clientes(tipo_cliente)
            print("\n===== CLIENTES FILTRADOS =====")
            for cliente in clientes:
                print(cliente)

        elif opcao == "3":
            clientes = criar_atributo_derivado()
            print("\n===== CLIENTES COM ATRIBUTO DERIVADO =====")
            for cliente in clientes:
                print(cliente)

        elif opcao == "4":
            clientes = ordenar_clientes_por_nome()
            print("\n===== CLIENTES ORDENADOS POR NOME =====")
            for cliente in clientes:
                print(cliente)

        elif opcao == "5":
            forma_pagamento = input("Digite a forma de pagamento: ")
            clientes = filtrar_clientes_por_pagamento(forma_pagamento)
            print("\n===== CLIENTES FILTRADOS POR FORMA DE PAGAMENTO =====")
            for cliente in clientes:
                print(cliente)

        elif opcao == "6":
            nome = input("Digite o nome do cliente: ")
            tipo = input("Digite o tipo do cliente (PJ ou PF): ")
            adicionar_cliente(nome, tipo)
            print("Cliente adicionado com sucesso!")

        elif opcao == "0":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
