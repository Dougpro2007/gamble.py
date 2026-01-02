#biblioteca RANDOM para aleatoriedade e OS para limpara o terminal
import random
import os

figuras = ["💎","🪙","👑"]

while True:
    try:    
        dinheiro_entrada = float(input("digite o valor que deseja inserir: "))
        break
    except ValueError:
        os.system("cls")
        print("insira um valor válido! \n")

dinheiro = dinheiro_entrada

os.system("cls")

print("R$",dinheiro, "\n")
print(figuras,"\n")

def gamble():
    global dinheiro
    figuras_choice = []

    resposta = input("deseja apostar? vc parece um cara de sorte (s/n) ")

    match(resposta.lower()):
        case "s":
            for _ in figuras:
                figuras_choice.append(random.choice(figuras))

            contagem = set(figuras_choice)
            mensagem = ""

            if len(contagem) == 3:
                ganho = (dinheiro/100 * 30)
                dinheiro -= ganho

                mensagem = f"nao foi dessa vez, tente novamente! quem não joga não recupera! -{ganho:.2f} \n"

                print(figuras_choice, "\n" , mensagem)
            elif len(contagem) == 2:
                ganho = (dinheiro/100 * 5)
                dinheiro += ganho

                mensagem = f"quase! voce esta com sorte! ganho normal! +{ganho:.2f} \n"
            else:
                ganho = (dinheiro/100 * 20)
                dinheiro += ganho

                mensagem = f"tirou a sorte grande, grande ganho! +{ganho:.2f} \n"
            
            #bloco doq vai pro terminal 
            #comando os limpa o terminal
            os.system("cls")
            print("dinheiro: R$", f"{dinheiro:.2f}", "\n")
            print(figuras_choice, "\n\n" , mensagem)
            
            resposta = input("deseja jogar novamente?(s/n) ")

            if resposta == "s":
                gamble()
            else:
                print("fim do programa\n")

        case "n":
            print("fim do programa\n")
        case _:
            print("digite uma resposta valida!\n")
            gamble()
gamble()