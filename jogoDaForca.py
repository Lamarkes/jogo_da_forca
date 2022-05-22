# Projeto referente a segunda avaliação de Algoritimos e Logica de programação!
import random  # Importa o pacote "random" para utilizar na escolha aleatoria das palavras
from EstruturaBoneco import *

print("Bem-Vindo ao Jogo da Forca: ")  # Mensagem de bem-vindo ao jogador
acertos = 0  # contabiliza a contagem de acertos
erro = 0  # contabiliza a contagem de erros
letras_corretas = ''
palavra_secreta = "_ "
palavras = ["tubarão", "leão", "gato", "rato", "sapo", "gia", "lagarto", "galinha", "papagaio", "raposa",
            "tigre-branco", "peixe-palhaço", "piton", "cobra", "cachorro", "escorpião", "tartaruga", "elefante",
            "girafa", "hipopotamo", "bufalo", "tucano", "baleia", "guaxinin", "onça", "leopardo", "capivara",
            "crocodilo", "arara-azul", "leão marinho", "arraia", "ornitorrinco", "rã", "sapo-boi", "pantera",
            "flamingo", "pica-pau", "zebra", "rato-toupeira-pelado", "peixe-leão", "rã-titicaca", "salamandra-axolotl",
            "macaco-narigudo", "abelha", "vespa", "dragão-de-komodo", "golfinho", "orca", "dromedario", "andorinha",
            "babuino", "lobo", "mico-leão-dourado", "naja", "sagui", "vaca"]  # Lista das palavras que serão utilizadas no jogo

advinha = random.choice(palavras)  # Codigo para escolher a palavra aleatoria para ser utilizada no jogo
advinha = advinha.upper()  # acessibilidade com letras maiusculas e minusculas
contador = 0  # contador para utilizar no laço de repetição
letras = len(advinha)  # obter o número de letras da palavra escolhida
mensagem = ''
print(forca)  # mostra a forca do joguinho
while contador < letras:  # inicia o laço de repetição
    print(palavra_secreta, end="")
    contador += 1
advinha_letra = (advinha[0::])
while acertos != letras and erro != 6:
    teste = input("\nInforme uma letra: ").upper()
    if teste == advinha:
        print("Acertou em cheio!, Parabainx.")
        break
    while teste in advinha_letra:
        print(estrutura_boneco[erro])
        print("Acertou!")
        acertos += advinha.count(teste)
        letras_corretas += teste + " "
        mensagem = ''
        print(mensagem)
        if acertos == letras:
            print("Acertou tudo!")
            print("Meus parabéns!")
        for teste in advinha_letra:
            if teste in letras_corretas:
                mensagem += teste + ' '
            else:
                mensagem += '_ '
        print(mensagem)
        break
    else:
        print("Errou! Tente novamente!")
        erro += 1
        print(estrutura_boneco[erro])
        print(mensagem)
        if erro >= 6:
            print("Errou tudo, Boa sorte na proxima vez!")
            print("A palavra era: ", advinha)
