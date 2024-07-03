def The_ancient_cipher(number):
    pass_ = 'Ваш пароль: '
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_

print(The_ancient_cipher(int(input('Введите число: '))))