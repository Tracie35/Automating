from random import choice

animes = [
    ['naruto', 'Fairy Tail', 'Dragon Ball Z'],
    ['bleach', 'Black Clover', 'Death Note'],
    ['classroom assassin', 'Code Geass', 'Attack on Titan'],
    ['one piece', 'Sailor Moon', 'My Hero Academia']
]
mood =[
    ['happy', 'sad', 'excited', 'bored']
]
mood_anime_map = {
    'happy': ['naruto', 'Fairy Tail', 'Dragon Ball Z', 'Sailor Moon'],
    'sad': ['bleach', 'Death Note', 'Attack on Titan'],
    'excited': ['classroom assassin', 'Code Geass', 'My Hero Academia'],
    'bored': ['one piece', 'Black Clover']
}

print(choice(mood))

print('What mood are you in? ')
mood = input()

if mood in mood_anime_map:
    print('Here are some anime recommendations for your mood:')
    for anime in mood_anime_map[mood]:
        print(anime)
else:
    print('Sorry, we dont have any anime recommendations for that mood.')
