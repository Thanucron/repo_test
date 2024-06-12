meme_dict = {
    'LOL':'odpowiedź na coś zabawnego',
    'CRINGE': 'coś dziwnego lub wstydliwego',
    'ROFL': 'odpowiedź na żart',
    'SHEESH': 'lekka dezaprobata',
    'CREEPY': 'straszny, złowieszczy',
    'AGGRO': 'stać się agresywnym/zły'
}

try:
    word = str(input('Wpisz słowo: '))
except ValueError:
    print('Wpisz słowo')
if word in meme_dict.keys():
    print(word, ':', meme_dict[word])
else:
    print('nie ma tego słowa')

ppl_dict = {
    'Natan': 16,
    'Wojtek': 31,
    'Sandra': 45,
    'Maciej': 7,
    'Zdzisław': 63
}
new_ppl = {'Piotr': 25}
ppl_dict.update(new_ppl)
print(ppl_dict)

del ppl_dict['Piotr']

print(bool('Maciej' in ppl_dict))

for imie, wiek in ppl_dict.items():
    print(imie, ":", wiek)
