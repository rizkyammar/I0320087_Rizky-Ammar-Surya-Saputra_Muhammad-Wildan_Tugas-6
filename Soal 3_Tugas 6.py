for number in range(10,25):
    for i in range(2, number):
        if number % i == 0:
            print(number, "bukan prima")
            break
    else:
        print(number, "adalah bilangan prima") 