import json


#opção 1
def importar_perguntas():
   try:
        with open("perguntas.json", "r", encoding="utf-8") as f:
            Perguntas=json.load(f)
        return Perguntas
   except FileNotFoundError:
       print("Erro: O ficheiro não existe. Verifique a existência dele e depois, tente novamente.")
   except json.JSONDecodeError:
       print("Erro: O conteudo presente no ficheiro de perguntas não é um conteudo json.")

def guardar_pontuacuao(pont,f):
    with open("pontuacoes.json","w", encoding="utf-8") as f:
        json.dump(pont, f, ensure_ascii=False, indent=4)

#opção 2
def importar_pontuacao():
    try:
        with open("pontuacoes.json","r", encoding="utf-8") as f:
            pontuacao=json.load(f)
        return pontuacao
    except FileNotFoundError:
         print("Erro: O ficheiro não existe. Verifique a existência dele e depois, tente novamente.")
    except json.JSONDecodeError:
       print("Erro: O conteudo presente no ficheiro onde ficam as pontuações não é um conteudo json.")
