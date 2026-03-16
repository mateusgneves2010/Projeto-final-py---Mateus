import random
import json
import files

#opção 1
'''
def sortear_perguntas_facil(lista_facil):
    lista_final_facil=[]
    for i in lista_facil:
        while True:
            pergunta = random.choice(lista_facil)
            if pergunta in lista_final_facil:
                continue
            lista_final_facil.append(pergunta)
            break
    return lista_final_facil
def sortear_perguntas_medio(lista_medio):
    lista_final_medio = []
    for i in lista_medio:
        while True:
            pergunta = random.choice(lista_medio)
            if pergunta in lista_final_medio:
                continue
            lista_final_medio.append(pergunta)
            break
    return lista_final_medio
def sortear_perguntas_dificil(lista_dificil):
    lista_final_dificil=[]
    for i in lista_dificil:
        while True:
            pergunta=random.choice(lista_dificil)
            if pergunta in lista_final_dificil:
                continue
            lista_final_dificil.append(pergunta)
            break
    return lista_final_dificil

def sortear_peguntas_geral(lista_geral):
    lista_final_geral=[]
    for i in lista_geral:
        while True:
            pergunta=random.choice(lista_geral)
            if pergunta in lista_final_geral:
                continue
            lista_final_geral.append(pergunta)
            break
    return lista_final_geral
'''
def escolher_dificuldade():
        while True:
            print("Escolhe o nível de dificuldade:")
            print("1 | Fácil")
            print("2 | Médio")
            print("3 | Difícil")
            print("4 | Insano (Todas as dificuldades)")
            try:
                escolha_dificuldade=int(input("Opção: "))
                perguntas=files.importar_perguntas()
                if escolha_dificuldade==1:
                    perguntas_facil_list=[]
                    for i in perguntas:
                        if i["Dificuldade"]=="Fácil":
                            perguntas_facil_list.append(i)
                    perguntas_facil=random.sample(perguntas_facil_list, 10, counts=None)
                    print(perguntas_facil)
                    return perguntas_facil
                    #Acionar a função sortear_perguntas_facil
                elif escolha_dificuldade==2:
                    perguntas_medio_list=[]
                    perguntas_medio=[]
                    for i in perguntas:
                        if i["Dificuldade"]=="Médio":
                            perguntas_medio_list.append(i)
                    random.sample(perguntas_medio_list, 10, counts=None)
                    return perguntas_medio                    
                elif escolha_dificuldade==3:
                    perguntas_dificil_list=[]
                    perguntas_dificil=[]
                    for i in perguntas:
                        if i["Dificuldade"]=="Difícil":
                            perguntas_dificil_list.append(i)
                    random.sample(perguntas_dificil_list, 10, counts=None)
                    return perguntas_dificil
                elif escolha_dificuldade==4:
                    
                    #Acionar a função sortear_perguntas_geral
                    print("Jogo ainda não está feito seu tótó")
                    break
                else:
                    print("Escolhe pelo menos uma opção...")
            except ValueError:
                print("Erro: deves introduzir um número.")


        
#opção 2

def mostrar_top10(lista):
   pontuacoes_ordenadas=sorted(lista, key=lambda x: x["Pontuação"], reverse=True)
   return pontuacoes_ordenadas

pontuacoes_file=files.importar_pontuacao()


#print("Em ordenação...")
#opção 3

    

#escolher_dificuldade()


#Bloco de testes:

#Bloco de testes: