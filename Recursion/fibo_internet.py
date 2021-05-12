fibonacci_cache = {}


def fibonacci2(n):
    # if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci2(n - 1) + fibonacci2(n - 2)

    # cache the value and return it
    fibonacci_cache[n] = value

    return value


# warning! the next loop is slow without caching
for n in range(1, 1001):
    print(n, ":", fibonacci2(n))