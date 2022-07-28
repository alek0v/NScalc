def let(c, key):  # Переведення чисел в символи та навпаки (для систем числення > 10)
    lett = [chr(ch) for ch in range(ord('A'), ord('Z') + 1)]
    num = [int(i) for i in range(10, 36)]
    if key == 'to':
        return lett[num.index(c)]
    elif key == 'fr':
        return num[lett.index(c)]

def to10(s, d):  # Переведення в 10 СЧ
    out = 0
    step = [int(j) for j in range(len(s) - 1, -1, -1)]
    for i in range(len(s)):
        if str(s[i]).isalpha():
            s[i] = let(s[i].upper(), 'fr')
        out += int(s[i]) * d ** step[i]
    return out

def fr10(s, d):  # Переведення з 10 СЧ
    ost = []
    while s >= d:
        ost.append(s % d)
        s //= d
    ost.append(s)
    for i in range(len(ost)):
        if 9 < ost[i] < d:
            ost[i] = let(ost[i], 'to')
    return ost[::-1]

def prov(s, d):  # Помилка, якщо введене число більше за введену СЧ
    h = True
    while h == True:
        for i in range(len(s)):
            if str(s[i]).isalpha():
                s[i] = let(s[i].upper(), 'fr')
            if int(s[i]) >= int(d):
                if int(s[i]) > 9:
                    s[i] = let(s[i], 'to')
                print(f'\nЧисла {s[i]} немає в {d}-ковій системі числення.')
                s = [c for c in input(f"Введіть ваше {d}-кове число: ")]
            else:
                h = False
    return s

def prov2(a):  # Помилка, якщо введене значення не є числовим
    while not a.isdigit():
        a = input("Помилка. Введіть число: ")
    return a

def prov3(a):  # Помилка, якщо введене значення не є десятковим числом
    while not a.isdigit():
        a = input("Помилка. Введіть десяткове число: ")
    return a

def prov4(a):  # Помилка, якщо введена СЧ перевищує максимальну, тобто 37
    while int(a) > 37:
        a = input("\nМаксимальна система числення в даній програмі: 37.\nПовторіть введення: ")
        a = prov2(a)
    return a

def one_more(q):  # Перевірка коректності вхідної відповіді
    while True:
        if q.lower() == "т" or q.lower() == "так":
            return True
        elif q.lower() == 'н' or q.lower() == 'ні':
            return False
        else:
            q = input('Помилкові вхідні дані. Введіть т(так), н(ні): ')

print("\nПереведення систем числення.")
print("Максимальна система числення в даній програмі: 37.")
print('Максимальне число для 37-кової системи числення - Z (36 в десятковій).')
m = True
while m == True:  # Цикл, якщо користувач захоче виконати ще одне перетворення
    d = input('\nВведіть початкову систему числення: ')
    d = prov2(d)
    d = prov4(d)
    d = int(d)

    c = input("Введіть кінцеву систему числення: ")
    c = prov2(c)
    c = prov4(c)
    c = int(c)

    if d == 10: # Якщо початкова СЧ - десяткова
        s = input(f"Введите ваше {d}-ричное число: ")
        s = prov3(s)
        print(f'\nОтвет в {c}-ричной системе счисления: ', *fr10(int(s), c), sep='')
    
    elif c == 10:  # Якщо кінцева СЧ - десяткова
        s = [c for c in input(f"Введіть ваше {d}-кове число: ")]
        s = prov(s, d)
        print(f"\nВідповідь в {c}-ковій системі числення: {to10(s, d)}")

    else: # Будь-які СЧ
        s = [c for c in input(f"Введіть ваше {d}-кове число: ")]
        s = prov(s, d)
        s = to10(s, d)
        print(f'\nВідповідь в {c}-ковій системі числення: ', *fr10(s, c), sep='')

    m = one_more(input("\nВиконати ще одне переведення? (т/н): "))

input("\nНатисніть 'Enter' для завершення роботи програми: ")