from random import choice 

# list of animes
animes = [['naruto', 'bleach', 'classroom assassin', 'one piece', 'series'],
          ['Fairy Tail', 'Black Clover', 'Code Geass', 'Sailor Moon', 'series'],
          ['Dragon Ball Z', 'Death Note', 'Attack on Titan', 'My Hero Academia', 'series']]

# print random anime from list
print(choice(animes))

#mood
print('what mood are you in? ')
mood=input()

#loop through and find matching mood
for item in animes:
    if item [1] == mood:
        print[mood+ 'anime:'+ item[0]]
