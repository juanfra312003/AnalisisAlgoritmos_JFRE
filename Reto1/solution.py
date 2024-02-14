def problem_1(limit):
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def problem_2(limit):
    a, b = 1, 2
    result = 0
    while a <= limit:
        if a % 2 == 0:
            result += a
        aux = a
        a = b
        b = aux + b
    return result

def problem_3(number):
    i = 2
    while i * i <= number:
        if number % i != 0:
            i += 1
        else:
            number = number // i
    return number


def problem_4():
    largest = 0
    for i in range(1, 999):
        for j in range(1, 999):
            product = i * j
            if str(product) == str(product)[::-1] and product > largest:
                largest = product
    return largest

def problem_5(number):
    cumplio = False
    actualNumber = 0
    while (cumplio == False) :
        actualNumber += 1
        cumplio = divisibleByAll_aux_problem_5(actualNumber, number)
    return actualNumber

def divisibleByAll_aux_problem_5(number, limit):
    for i in range(1, limit + 1):
        if number % i != 0:
            return False
    return True