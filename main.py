import random
mainmotor=True
while mainmotor:
    essaie = -1
    score = 0
    borne_minimale = int(input('Quel est votre borne minimal?:'))
    borne_maximale = int(input('Quel est votre borne maximale?:'))
    valeur = random.randint(borne_minimale, borne_maximale)
    submotor = True
    while submotor:
        essaie = int(input('Entrez votre essai :'))
        if essaie == valeur:
            score = score + 1
            print('Vous avez reussi en:', score, 'essaie(s).')
            redo = (input('Voulez-vous recommencer?(x/o):'))
            if redo == 'x':
                exit()
            elif redo == 'o':
                submotor = False
            else:
                print('error')

        elif essaie > valeur:
            score = score + 1
            print('Mauvais choix, le nombre est plus petit que', essaie, ' ')
        elif essaie < valeur:
            score = score + 1
            print('Mauvais choix, le nombre est plus gros que', essaie, ' ')


