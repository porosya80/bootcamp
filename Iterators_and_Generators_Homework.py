import random


def gensquares(N):
    for i in range(N):
        yield i ** 2


def randinit(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


if __name__ == "__main__":
    for x in gensquares(10):
        print(x)
    for num in randinit(1, 10, 12):
        print (num)