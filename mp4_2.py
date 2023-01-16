# L'utilisateur choisi un des 5 signes à l'aide du pavé numérique (de 0 à 4), utiliser table ASCII

#  L'utilisateur affrontera l'ordinateur, qui jouera un des 5 signes aléatoirement pour plus d'équitabilité

# La partie se joue en 3 rounds GAGNANT

# Afficher le résultat de la manche à chacune d'entre elle, ainsi que de la partie en général

# Affichage à la fin des trois rounds de si l'utilisateur gagne ou perd

from random import randint

user_sign = 0
ai_sign = 0
user_wins = 0
ai_wins = 0
round_num = 1
signs_list=["Pierre","Papier","Ciseaux","Lézard","Spock"]

while user_wins < 3 and ai_wins < 3:
    print(f"Round {round_num}")

    # Définition du signe de chacun des participants
    user_sign=signs_list[int(input("Veuillez choisir un signe (0: Pierre, 1 : Papier, 2 : Ciseaux, 3 : Lézard, 4 : Spock) : "))]
    ai_sign=signs_list[randint(0,4)]

    # Résultat du round

    # Cas d'égalité
    if user_sign == ai_sign:
        print(f"Signe joueur => {user_sign} / {ai_sign} <= Signe ordinateur")
        print(f"Egalité (Score joueur {user_wins} / {ai_wins} Score ordinateur)\n")
        round_num = round_num+1

    # Cas de victoire de l'utilisateur
    elif user_sign == signs_list[0] and ai_sign == (signs_list[2] or signs_list[3]) or user_sign == signs_list[1] and ai_sign == (signs_list[0] or signs_list[4]) or user_sign == signs_list[2] and ai_sign == (signs_list[1] or signs_list[3]) or user_sign == signs_list[3] and ai_sign == (signs_list[4] or signs_list[1]) or user_sign == signs_list[4] and ai_sign == (signs_list[2] or signs_list[0]):
        print(f"Signe joueur => {user_sign} / {ai_sign} <= Signe ordinateur")
        print(f"Victoire (Score joueur {user_wins+1} / {ai_wins} Score ordinateur)\n")
        user_wins += 1
        round_num = round_num+1

    # Cas de défaite de l'utilisateur
    else:
        print(f"Signe joueur => {user_sign} / {ai_sign} <= Signe ordinateur")
        print(f"Défaite (Score joueur {user_wins} / {ai_wins+1} Score ordinateur)\n")
        ai_wins += 1
        round_num = round_num+1

    print(f"{ai_wins}")

# Résultats de la partie
if user_wins == 3:
    print("**********Vous avez gagné la partie !*********")

if ai_wins == 3:
    print("**********Vous avez perdu la partie !*********")


        

