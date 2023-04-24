while True:
    value = input('Введите дробное число\n')
    try:
        number = float(value)
        print(number)
        break
    except ValueError:
        print('Это не число')