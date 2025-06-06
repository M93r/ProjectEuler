from math import sqrt

def square_root(n1):
    return int(sqrt(n1))


def decomposition(n2):
    crossing = 2
    prime = []
    square = square_root(n2)
    while crossing < square:
        if n2 % crossing == 0:
            prime.append(crossing)
            n2 = int(n2 / crossing)
        else:
            crossing += 1
    return prime

def largest_factor(n3):
    print(decomposition(n3)[-1]) 

largest_factor(600851475143)
