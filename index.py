# Define a função que recebe as vitórias e derrotas como parâmetros para calcular o nível do jogador.
def calcular_ranque(vitorias, derrotas):
    # Calcula o saldo de Rankeadas, subtraindo as derrotas das vitórias.
    ranked = vitorias - derrotas

    # Define o nível do jogador com base na quantidade de vitórias.
    if vitorias <= 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    # Retorna a mensagem com o saldo e o nível do herói.
    return f"O Herói tem de saldo de {ranked} e está no nível de {nivel}."

# Solicita ao Usuário as vitórias e derrotas.
vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

# Chama a função e imprime o resultado.
resultado = calcular_ranque(vitorias, derrotas)
print(resultado)