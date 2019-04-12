import requests


apiUrl = 'https://superheroapi.com/api/2137552436292179';
fighter_id = 5

g = requests.get(('f{apiUrl}/{fighter_id}'))

print('g.text')
