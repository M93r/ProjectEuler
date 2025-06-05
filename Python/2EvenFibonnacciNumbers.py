def fibonacci(stop):
    """Create a list to store the fibonacci sequence"""
    a, b = 0, 1
    sequence = []
    sequence.append(a)
    sequence.append(b)
    sequence.append(b)
    while stop > b:
        a = b - a
        b = b + a
        sequence.append(b)
    return sequence

def even_fibonacci():
    """Find all even numbers"""
    even_list = []
    for number in fibonacci(4000000):
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sum_even_fibonacci():
    total = 0
    for number in even_fibonacci():
        total += number
    print(total)

sum_even_fibonacci()
