import re


def Cyr(txt):
    return bool(re.search('[а-яА-Я]', txt))


eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
       4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
      4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
txt = input('give my a word: ').upper()
if Cyr(txt):
    print(
        f'Cтоимость слова: {sum([j for i in txt for j, e in ru.items() if i in e])}')
else:
    print(f'Cost: {sum([j for i in txt for j, e in eng.items() if i in e])}')
