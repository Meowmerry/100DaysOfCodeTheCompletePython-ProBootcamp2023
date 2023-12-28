
def prime_checker(number, div=2):

    if number < 2:
        print("It's not a prime number.")
        return False
    if number == div:
        print("It's a prime number.")
        return True
    if number % div == 0:
        print("It's not a prime number.")
        return False
    return prime_checker(number, div + 1)


prime_checker(13)  # It's a prime number.
prime_checker(87)  # It's not a prime number.
prime_checker(97)  # It's a prime number.
prime_checker(66)  # It's not a prime number.
prime_checker(47)  # It's a prime number.


def prime_checker(number):
    isPrime = True

    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(13)  # It's a prime number.
prime_checker(87)  # It's not a prime number.
prime_checker(97)  # It's a prime number.
prime_checker(66)  # It's not a prime number.
prime_checker(47)  # It's a prime number.
