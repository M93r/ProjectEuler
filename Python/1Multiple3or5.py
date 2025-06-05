
def multiples(m1=3, m2=5, stop=1000):
    """Find the multiples 3 and 5"""
    count = 1
    sum = 0
    while count < stop:
        if count % m1 == 0 and count % m2 == 0:
            sum += count
            count += 1
        elif count % m1 == 0:
            sum += count
            count += 1
        elif count % m2 == 0:
            sum += count 
            count += 1
        else:
            count += 1
    print(sum)

multiples()

