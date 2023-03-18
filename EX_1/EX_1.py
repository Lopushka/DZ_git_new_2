print('Заполните список.Цифры вводить через ",".')
tbl = map(int, (input().split(',')))
q = int(input('Введите число: '))
cnt = 0
for i in tbl:
    if i == q:
        cnt += 1
print (f'Кол-во чисел "{q}" в списке: {cnt if cnt!=0 else -1}')

