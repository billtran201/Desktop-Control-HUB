

def main():
    with open("jarvis/application/math_app/data/prime_number.txt", "w") as wiper:
        wiper.write("")

    writer = open("jarvis/application/math_app/data/prime_number.txt", "a", encoding="utf-8")

    number = 1

    while(number < 100000000):
        if is_prime(number):
            writer.write(str(number) + "\n")
        number += 1

    return



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()