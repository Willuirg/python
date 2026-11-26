import sqlite3

con = sqlite3.connect(":memory:")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE servicos(
 id_serv INTEGER PRIMARY KEY,
 nome_cliente text NOT NULL,
 preco REAL, 
 equipamento text NOT NULL,
 desc_serv text NOT NULL
 )
""")

for i in range(4):
    print(f"\n ---Cadrasto {i + 1}° produto---")
    nome = input("Digite o nome do cliente: ")
    preco = float(input("Digite o preço: "))
    equipamento = input("Digite o equipamento utilizado: ")
    descricao = input("Digite a descrição do serviço: ")

    cursor.execute("""
    INSERT INTO servicos(nome_cliente, preco, equipamento, desc_serv) VALUES (?, ?, ?, ?)""",
    (nome, preco, equipamento, descricao)
    )

con.commit()
print("\n - Serviços cadastrados - ")
cursor.execute("SELECT * FROM servicos")
produtos = cursor.fetchall()

for id_serv, nome_cliente, preco, equipamento, descricao in produtos:
    print(f"ID: {id_serv} - NOME: {nome_cliente} - PREÇO: R$ {preco:.2f} - EQUIPAMENTO {equipamento} - DESCRIÇÃO {descricao}")

con.close()


