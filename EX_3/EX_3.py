eng = 'QWERTYUIOPASDFGHJKLZXCVBNM'

rus = 'ЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'

glossary_eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
                4: 'FHVWY', 5: "K", 8: 'JX', 10: 'QZ'}
glossary_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
               4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФШЪ'}

txt = input('Введите слово: ').upper()

if txt[0] in eng:
    s = 0
    for i in txt:
        for j, k in glossary_eng.items():
            if i in k:
                s += j
    print(f'cost: {s}')
else:
    if txt[0] in rus:
        s = 0
        for i in txt:

            for j, k in glossary_ru.items():
                if i in k:
                    s += j
    print(f'стоимость слова: {s}')
