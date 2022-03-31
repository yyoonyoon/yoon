def even_number_plus(a,b):
    total = 0
    for i in range(a, b):
        if (i % 2 == 0):
            total += i
    print(total)

even_number_plus(1,101)