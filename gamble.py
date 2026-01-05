#biblioteca RANDOM para aleatoriedade e OS para limpar o terminal
import random
import os

#variavel do jackpot
figuras = ["💎","🪙","👑"]

#variaveis do status
ganhos_status = 0
perdas_status = 0
giros_status = 0

while True:
    try:    
        dinheiro_entrada = float(input("digite o valor monetário que deseja inserir para poder jogar: "))
        break
    except ValueError:
        os.system("cls")
        print("insira um valor válido! \n")

dinheiro = dinheiro_entrada

os.system("cls")

print("R$",dinheiro, "\n")
print(figuras,"\n")

#funções essenciais do programa
def mostrar_status():
    os.system("cls")

    print("GAMBLE.PY STATUS \n")

    print(f"salto atual: R${dinheiro:.2f}")
    print(f"ganhos totais: R${ganhos_status:.2f}")
    print(f"perdas totais: R${perdas_status:.2f}")
    print(f"giros totais: {giros_status}")

    resposta = input("\n pressione qualquer tecla pra sair ")
    
    match(resposta):
        case _:
            os.system("cls")
            gamble()

def gamble():
    global dinheiro
    global ganhos_status
    global perdas_status
    global giros_status

    figuras_choice = []

    resposta = input("\n deseja apostar? ( s / n / status ) ")

    match(resposta.lower()):
        case "s":
            giros_status += 1
            for _ in figuras:
                figuras_choice.append(random.choice(figuras))

            contagem = set(figuras_choice)
            mensagem = ""

            if len(contagem) == 3:
                ganho = 5
                perdas_status += ganho
                dinheiro -= ganho

                mensagem = f"nao foi dessa vez, tente novamente! quem não joga não recupera! -{ganho:.2f} \n"

                print(figuras_choice, "\n" , mensagem)
            elif len(contagem) == 2:
                ganho = 0.5
                ganhos_status += ganho
                dinheiro += ganho

                mensagem = f"quase! voce esta com sorte! ganho normal! +{ganho:.2f} \n"
            else:
                ganho = 3
                ganhos_status += ganho
                dinheiro += ganho

                mensagem = f"tirou a sorte grande, grande ganho! +{ganho:.2f} \n"
            
            #bloco que vai ser exibido no terminal 
            os.system("cls")
            print(f"dinheiro: R${dinheiro:.2f} \n") 
            print(figuras_choice, "\n\n" , mensagem)
            
            resposta = input("deseja jogar novamente? ( s / n / status ) ")

            
            match(resposta.lower()):
                case "s":
                    os.system("cls")
                    gamble()
                case "status":
                    mostrar_status()
                case "n":
                    print("fim do programa!")
                case _:
                    os.system("cls")
                    print("digite uma resposta valida!\n")
                    gamble()

        case "n":
            print("fim do programa\n")
        case "status":
            mostrar_status()
        case _:
            os.system("cls")
            print("digite uma resposta valida!\n")
            gamble()

gamble()