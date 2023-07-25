import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            veiculo TEXT NOT NULL,
            valor_total REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')

    conexao.commit()
    conexao.close()

def inserir_cliente(nome, veiculo, valor_total):
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO clientes (nome, veiculo, valor_total) VALUES (?, ?, ?)', (nome, veiculo, valor_total))

    conexao.commit()
    conexao.close()

def inserir_servico(cliente_id, descricao, valor):
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO servicos (cliente_id, descricao, valor) VALUES (?, ?, ?)', (cliente_id, descricao, valor))

    conexao.commit()
    conexao.close()

def recuperacao_simples():
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM clientes')

    for row in cursor.fetchall():
        print(row)

    conexao.close()

def filtro_por_veiculo(veiculo):
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM clientes WHERE veiculo = ?', (veiculo,))

    for row in cursor.fetchall():
        print(row)

    conexao.close()

def atributo_derivado():
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT clientes.id, clientes.nome, clientes.veiculo, clientes.valor_total, SUM(servicos.valor) AS valor_servicos '
                   'FROM clientes '
                   'LEFT JOIN servicos ON clientes.id = servicos.cliente_id '
                   'GROUP BY clientes.id')

    for row in cursor.fetchall():
        print(row)

    conexao.close()

def ordenacao_por_valor_total():
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM clientes ORDER BY valor_total DESC')

    for row in cursor.fetchall():
        print(row)

    conexao.close()

def filtro_por_valor_servicos_minimo(valor_minimo):
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT clientes.id, clientes.nome, clientes.valor_total, SUM(servicos.valor) AS valor_servicos '
                   'FROM clientes '
                   'LEFT JOIN servicos ON clientes.id = servicos.cliente_id '
                   'GROUP BY clientes.id '
                   'HAVING valor_servicos >= ?', (valor_minimo,))

    for row in cursor.fetchall():
        print(row)

    conexao.close()

def juncao_entre_tabelas():
    conexao = sqlite3.connect('oficina.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT clientes.nome, clientes.veiculo, COUNT(servicos.id) AS total_servicos '
                   'FROM clientes '
                   'LEFT JOIN servicos ON clientes.id = servicos.cliente_id '
                   'GROUP BY clientes.id')

    for row in cursor.fetchall():
        print(row)

    conexao.close()

def exibir_menu():
    print("1. Inserir cliente")
    print("2. Inserir serviço")
    print("3. Recuperação simples (SELECT)")
    print("4. Filtro por veículo (WHERE)")
    print("5. Atributo derivado")
    print("6. Ordenação por valor total (ORDER BY)")
    print("7. Filtro por valor mínimo de serviços (HAVING)")
    print("8. Junção entre tabelas")
    print("0. Sair")

def main():
    criar_tabelas()

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            veiculo = input("Digite o veículo do cliente: ")
            valor_total = float(input("Digite o valor total do cliente: "))
            inserir_cliente(nome, veiculo, valor_total)

        elif opcao == "2":
            cliente_id = int(input("Digite o ID do cliente: "))
            descricao = input("Digite a descrição do serviço: ")
            valor = float(input("Digite o valor do serviço: "))
            inserir_servico(cliente_id, descricao, valor)

        elif opcao == "3":
            recuperacao_simples()

        elif opcao == "4":
            veiculo = input("Digite o veículo desejado: ")
            filtro_por_veiculo(veiculo)

        elif opcao == "5":
            atributo_derivado()

        elif opcao == "6":
            ordenacao_por_valor_total()

        elif opcao == "7":
            valor_minimo = float(input("Digite o valor mínimo de serviços: "))
            filtro_por_valor_servicos_minimo(valor_minimo)

        elif opcao == "8":
            juncao_entre_tabelas()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
