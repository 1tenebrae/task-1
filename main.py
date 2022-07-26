import requests
import json


our_user = requests.get('https://reqres.in/api/users/10').json()['data']

print(f"ID: {our_user['id']}\n\n\
last name: {our_user['last_name']}\n\
first name: {our_user['first_name']}\n")

input('Press ENTER to exit')