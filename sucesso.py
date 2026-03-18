pontuacao = 0
pontuacao_final = pontuacao
rank = 0
print("1 | Sucesso com 0 pontos")
print("2 | Sucesso com 25 pontos")
print("3 | Sucesso com 50 pontos")
print("4 | Sucesso com 75 pontos")
print("5 | Sucesso com 90 pontos")
print("6 | Sucesso com 100 pontos")
opcao = int(input("Escolhe a opção de teste: "))

if opcao == 1:
    if rank >= 0 and rank <= 24:
        rank = "D"
    print("\n")
    print("Da próxima vez, vais melhor e lê as perguntas, é necessário...")
    print(f"Rank Final: {rank}")
    print(f"Total de pontuação: {pontuacao}")
elif opcao == 2:
    rank += 25
    if rank >= 25 and rank <= 49:
        rank = "C"
    pontuacao += 25
    print("\n")
    print("Bem jogado, não foste o melhor mas pelo menos não tiveste um rank D.")
    print(f"Rank Final: {rank}")
    print(f"Total de pontuação: {pontuacao}")
elif opcao == 3:
    rank += 50
    if rank >= 50 and rank <= 74:
        rank = "B"
    pontuacao += 50
    print("\n")
    print("Bem jogado, só precisas de um pouco de prática e chegarás num rank alto.")
    print(f"Rank Final: {rank}")
    print(f"Total de pontuação: {pontuacao}")
elif opcao == 4:
    rank += 75
    if rank >= 75 and rank <= 89:
        rank = "A"
    pontuacao += 75
    print("\n")
    print("Bem jogado, daqui algum dia chegas ao Rank S.")
    print(f"Rank Final: {rank}")
    print(f"Total de pontuação: {pontuacao}")
elif opcao == 5:
    rank += 90
    if rank >= 90 and rank <= 99:
        rank = "S"
    pontuacao += 90
    print("\n")
    print("Excelente jogada, conseguiste um rank muito alto.")
    print(f"Rank Final: {rank}")
    print(f"Total de pontuação: {pontuacao}")
elif opcao == 6:
    rank += 100
    if rank == 100:
        rank = "P"
    pontuacao += 100
    print("\n")
    print("Não há palavra pra dizer, tu conquistaste esta dificuldade.")
    print(f"Rank Final: {rank}")
    print(f"Total de pontuação: {pontuacao}")