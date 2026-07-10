import random
import sys
while True:
    quotes = [
      "Got some rare things on sale, stranger! 😎",
      "What are ya buyin'?",
      "What are ya sellin'?",
      "Ahhh... I'll buy it at a high price!",
      "Hehehe... Thank you!",
      "Not enough cash, stranger.",
      "Come back anytime.",
      "Stranger, stranger! Now that's a weapon!",
      "Is that all, stranger?",
      "Hehehehehe...",
      "Heh heh heh... Thank you!",
      "Ahh, I'll buy it at a high price.",
      "I'll pay a high price for that!",
      "Got a selection of good things on sale, stranger!",
      "Hehehe... Welcome!",
    ]

    print("Frases clássicas do mercador do Resident Evil 4")
    escolha = input("Deseja continuar? S ou N : ")

    if escolha == "S":
        quote = random.choice(quotes)
        print(quote)
    elif escolha == "N":
        print("Ok! encerrando o programa.")
        break
    else:
        print("Digite uma opção válida.")
