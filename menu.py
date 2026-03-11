import logica
import files

def mostrar_menu():
    utilizador = input("-> Utilizador: ")
    while True:
        print("|================================================|")
        print("|---------------------Menu-----------------------|")
        print("|================================================|")
        print(f"Olá {utilizador}. Bem vindo ao Jogo de Perguntas.")
        print("\================================================/")
        print("1 | Jogar")
        print("2 | Pontuações")
        print("3 | Regras/Ajuda")
        print("4 | Sair")
        print("/================================================\ ")

        try:
            option = int(input("-> Opção: "))
            if option == 4:
                print("|================================================|")
                print("|---------------------Sair-----------------------|")
                print("\================================================/")
                print("")
                print("Obrigado por jogar\n")
                print("/================================================\ ")
                break
            elif option == 1:
                print("|================================================|")
                print("|--------------------Jogar-----------------------|")
                print("\================================================/")
                lista_perguntas=logica.escolher_dificuldade() 
                def mostrar_pergunta():
                    print("/-----------------\============/-----------------\ ")
                    print("|-----------------|==Pergunta==|-----------------|")
                    print("\-----------------/============\-----------------/")
                    questao=#criar uma outra função que vai buscar as informações...
                    opcoes=#criar uma outra função que vai buscar as informações...
                    print(questao)
                    print(opcoes)


                    '''
                    contador = 0
                    perguntas_ja_feitas = []
                    while contador <= 10:
                        for i in range(11):
                            print("\n")
                            print(f"Número {i}")
                            contador -= 1
                        return
                    '''
            elif option == 2:
                print("|================================================|")
                print("|------------------Pontuações--------------------|")
                print("\================================================/")
                pontuacao_file=files.importar_pontuacao()
                top10=logica.mostrar_top10(pontuacao_file)
                colocacao=1
                for i in top10:
                    nome=i["Nome"]
                    pontuacao=i["Pontuação"]
                    if colocacao<=10:
                        print(f"{colocacao}º - {nome}, com pontuação de {pontuacao} pontos")
                    colocacao+=1
                voltar_menu=input("\nPrima enter para continuar...")
                print(voltar_menu)
                print(" ")
                print("/================================================\ ")
            elif option == 3:
                print("|================================================|")
                print("|-----------------Regras/Ajuda-------------------|")
                print("\================================================/")
                print("")
                def mostrar_ajuda():
                    while True:
                        print("\n Opções de ajuda:")
                        print("1- Jogabilidade")
                        print("2- Pontuações")
                        print("3- Sair")
                        try:
                            escolha_ajuda=int(input("Introduz uma opção: "))
                            if escolha_ajuda==1:
                                print("1º passo: deve escolher a dificuldade que quer jogar. Pode escolher entre fácil, médio e difícil.")
                                print("\n2º passo: Vai aparecer as perguntas, na qual deve escrever a opção correta")
                                print("\n3º passo: no fim do jogo, vai poder ver a pontuação final.")
                            elif escolha_ajuda==2:
                                print("Aqui pode consultar a pontuação. Para sair, basta premir a tecla enter.")
                                voltar_ajuda=input(" : ")
                                print(voltar_ajuda)
                            elif escolha_ajuda==3:
                                break
                            else:
                                print("Erro: deve introduzir um número válido")
                        except ValueError:
                            print("Erro: deve introduzir um número válido")
                print("/================================================\ ")
            else:
                print("|================================================|")
                print("|-------------------ERRO--:(---------------------|")
                print("\================================================/")
                print("")
                print("Seu espertalhão, tens que meter um número que está no terminal. Abre outro terminal e seleciona um dos números que estão lá...")
                print("/================================================\ ")
                break
        except ValueError:
            print("Erro: deve ser introduzido um número.")


mostrar_menu()
