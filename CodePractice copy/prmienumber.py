def is_prime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Example usage:
number = 7
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


def prime_no(n):

    if n <= 1:
        return False
    return all(n % i != 0 for i in range( 2, int(n**0.5) + 1))

print(prime_no(2))


def prime_recrusion(n,i=2):

    if n <= 1:
        return False
    
    if n < i ** 2:
        return True
    if n % 2 == 0:
        return False
    
    prime_recrusion(n,i+1)

print(prime_recrusion(3))