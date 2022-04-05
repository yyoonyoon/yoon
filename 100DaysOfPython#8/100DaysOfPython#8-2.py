n = int(input("Check this number: "))
def prime_checker(number=n):
    for i in range(2, number):
        result = number % i
        if result != 0: #소수일 가능성이 있을 때.
            continue        
        else: #이미 나눠지는 수가 있어서 소수 가능성 없을 때.
            print("It is not prime number :(")
            break
    if i == number-1:
        print("It is prime number!!")


prime_checker(n)