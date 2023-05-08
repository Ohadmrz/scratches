
start_range = int(input("Insert start range: "))
end_range = int(input("Insert end range: "))
primes = []

for num in range(start_range, end_range+1):
    is_prime = True
    for i in range(2, int((num+2)/2)):
        if num % i == 0:
            # not prime
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(primes)