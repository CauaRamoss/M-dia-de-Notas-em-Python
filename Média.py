# Solicita ao usuário que insira as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
 
# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3
 
# Mostra o resultado ao usuário
print(f"A média das notas é: {media:.2f}")
