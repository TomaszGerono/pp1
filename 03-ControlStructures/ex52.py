def is_prime(number):
    if number <= 0:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

N = int(input("Enter the value of N: "))

prime_numbers = []
count = 0
number = 2

while count < N:
    if is_prime(number):
        prime_numbers.append(number)
        count += 1
    number += 1

is_N_prime = is_prime(N)

print(f"The first {N} prime numbers are: {prime_numbers}")

