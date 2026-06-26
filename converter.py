def converter(metros):
    """Converte metros para centímetros."""
    return metros * 100

print("====Conversor de Metros para Centímetros====")
metros = float(input("Digite o valor em metros: "))
centimetros = converter(metros)
print(f"{metros} metros é igual a {centimetros} centímetros.")