def result(num):
    result = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                result += str(i) + str(j)
    return result
print('Введите число: ')
print(result(int(input())))





