# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

weight =int(input('Введите максимальную грузоподъемность рюкзака: '))
# catalog = {}
# n = int(input('введите кол-во вещей в списке: '))
# for _ in range(n):
#     name = input('Название вещи: ')
#     catalog[name] = int(input('вес вещи: '))
# print(catalog)
catalog = {'палатка': 2, 'ложка': 5, 'лопата': 5, 'кремень': 6, 'вода': 7}
backpack_i = []
for k, v in catalog.items():
    sum_v = 0
    if sum_v <= weight:
        sum_v += v
        backpack_i.append(k)
        weight -= v
print(f'В рюкзак поместятся {", ".join(str(i) for i in backpack_i)}')
