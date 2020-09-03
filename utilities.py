def prime_number_generator(n):
    """
    this function returns the first n prime numbers
    Args:
        n: up to number
    Return:
        list of the first n prime numbers
    """
    prime_numbers = []
    for number in range(1, n + 1):
        for i in range(2, number):
            if (number % i) == 0:
                break
        else: 
            prime_numbers.append(number)
    return prime_numbers


def twin_prime_generator(n):
    """
    this function returns first n pairs of twin 
    primes numbers
    Args:
        n: up to number
    Return:
        list of the first n pairs of twin primes numbers
    """
    prime_numbers = prime_number_generator(n)
    twin_primes = []
    BASE = 2
    for number in prime_numbers:
        if number + BASE in prime_numbers:
            twin_primes.append((number, number + BASE))
    return twin_primes