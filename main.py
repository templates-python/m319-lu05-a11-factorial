def main_while():
    iterations = int(input('Give a number: '))
    count = 1
    fact = 1
    while count <= iterations:
        fact = fact * count
        count += 1
    print(fact)


def main_for():
    iterations = int(input('Give a number: '))
    fact = 1
    for count in range(1, iterations + 1):  # start from 1, and iterations+1 to ensure that upper bound is included
        fact = fact * count
    print(fact)


if __name__ == '__main__':
    main_while()
    main_for()
