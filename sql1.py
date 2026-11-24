import sqlite3

con = sqlite3.connect(":memory:")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE produtos(
 id_prod INTEGER PRIMARY KEY,
 nome text NOT NULL,
 preco REAL, 
 quantidade INTEGER
)
""")

for i in range(3):
    print(f"\n ---Cadrasto {i + 1}° produto---")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))

    cursor.execute("""
    INSERT INTO produtos(nome, preco, quantidade) VALUES (?, ?, ?)""",
    (nome, preco, quantidade)
    )

con.commit()

print("\n - produtos cadastrados no estoque - ")
cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

for id_prod, nome, preco, quantidade in produtos:
    print(f"ID: {id_prod} - NOME: {nome} - PREÇO: R$ {preco:.2f} - QUANTIDADE: {quantidade}")

con.close()