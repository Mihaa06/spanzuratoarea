from random import choice
pics=['''
=========||
    |    ||
         ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
    |    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   /     ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   / \   ||
         ||
         || ''',
]
word_list = [ 'macarena' , 'panamera' , 'metin2arena' , "onomatopee"]

def extrage_cuv() :
    return choice(word_list)

def play_game():
    cuv = extrage_cuv()
    how_dead_am_i = 0
    litere_ghicite = []
    castigat =  False
    print(cuv)
    while how_dead_am_i < len(pics):
        print(pics[how_dead_am_i])
        castigat = True
        for ch in cuv:
            if ch in litere_ghicite:
                print(ch,end='')
            else:
                print('_', end='')
                castigat=False
        print()
        if castigat:
            print("Bravo,boss!")
            break

        letter=input("Zi o litera")
        if letter in cuv and letter not in litere_ghicite:
            litere_ghicite.append(letter)
        else:
            how_dead_am_i += 1
    if not castigat:
        print(pics[how_dead_am_i])
        print("Ai cam murit ce sa zic")

play_game()