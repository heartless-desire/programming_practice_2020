def menu():
    print('1. Площадь круга')
    print('2. Площадь прямоугольника')
    print('3. Площадь треугольника')
    print('0. Выход')


def circle_area():
    r = float(input('Введите радиус круга:'))
    return 'Ответ: {}'.format(r**2*__import__('math').pi)


def rect_area():
    a, b = list(map(float, input('Введите стороны прямоугольника:').split()))
    return 'Ответ: {}'.format(a*b)


def triangle_area():
    print('1. По Герона')
    print('2. По высоте')
    ans = input()
    if ans == '1':
        a, b, c = list(map(float, input('Введите стороны треугольника:').split()))
        p = (a + b + c) / 2
        return 'Ответ: {}'.format((p*(p-a)*(p-b)*(p-c))**.5)
    elif ans == '2':
        a, h = list(map(float, input('Введите сторону и высоту, опущенную к ней:').split()))
        return 'Ответ: {}'.format(a*h/2)
    else:
        return 'Такого варианта нет!'


while True:
    menu()
    ans = input()

    if ans == '1':
        print(circle_area())
    elif ans == '2':
        print(rect_area())
    elif ans == '3':
        print(triangle_area())
    elif ans == '0':
        break
    else:
        print('Такого варианта нет')